# -*- coding: utf-8 -*-
"""从 en/instructions.md 生成 de/instructions.md：结构/样式/脚本不动，只替换可见文字。
定价：与美元版同数字平价（用户拍板 €45 而非 €44），德语数字格式「60 €」「1.400 €」。
三档 60/95/120 €；初级 220 €；中级 790 €；返利 20/44/145 €；封顶 210 €；上限 1.400 €；奖学金 44 €。"""
import io, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(BASE, '..', '..', 'content', 'en', 'instructions.md'), encoding='utf-8').read()

R = [
    # front matter / alt / hero
    ('title: "Coaching | Trance Mentorship | Eonun"', 'title: "Coaching | Trance-Mentoring | Eonun"'),
    ('description: "From enthusiast to the international stage: maximize what you learn at a fair price \u2014 and hear the progress"',
     'description: "Vom Enthusiasten zur internationalen B\u00fchne: maximaler Lernertrag zu einem fairen Preis \u2014 mit h\u00f6rbar schnellem Fortschritt"'),
    ('alt="Coaching | Trance Mentorship"', 'alt="Coaching | Trance-Mentoring"'),
    ('          From enthusiast to the international stage: maximize what you learn at a fair price \u2014 and hear the progress\n',
     '          Vom Enthusiasten zur internationalen B\u00fchne: maximaler Lernertrag zu einem fairen Preis \u2014 mit h\u00f6rbar schnellem Fortschritt\n'),
    # 课程 hero
    ('<h1 class="hero-title">Trance Mentorship</h1>', '<h1 class="hero-title">Trance-Mentoring</h1>'),
    ('<p>Since you\u2019ve read this far, take one more step.</p>', '<p>Wenn Sie schon so weit gelesen haben, gehen Sie den letzten Schritt.</p>'),
    ('<p>What I offer is straightforward: you deal with me directly; pricing and tiers are fully transparent, with no hidden fees; the knowledge is systematic; and the coaching lands on your actual tracks.</p>',
     '<p>Mein Angebot ist schlicht: Sie kommunizieren direkt mit mir; Preise und Leistungsstufen sind vollkommen transparent, ohne versteckte Kosten; das Wissen ist systematisch aufgebaut; und das Coaching zielt auf Ihre konkreten Tracks.</p>'),
    ('<p>Everything is built around one practical goal \u2014 tracks that are yours, and that hold up.</p>',
     '<p>Alles dreht sich um ein praktisches Ziel \u2014 Tracks, die Ihre eigenen sind und die bestehen.</p>'),
    ('<p>Whether you\u2019re just getting started or you\u2019re a producer or DJ looking to level up, there\u2019s a place for you here.<span style="color: #d9d9d9;"></span></p>',
     '<p>Ob Sie gerade erst anfangen oder Produzent bzw. DJ sind und den n\u00e4chsten Schritt wagen m\u00f6chten \u2014 hier ist ein Platz f\u00fcr Sie.<span style="color: #d9d9d9;"></span></p>'),
    ('<p style="margin-top: 0.6rem; font-size: 0.8rem; color: #888888; letter-spacing: 0.5px;">* Sessions available in English and Chinese</p>',
     '<p style="margin-top: 0.6rem; font-size: 0.8rem; color: #888888; letter-spacing: 0.5px;">* Sessions auf Chinesisch und Englisch m\u00f6glich</p>'),
    # 课程导航
    ('<h3 class="nav-title">Choose a Service</h3>', '<h3 class="nav-title">W\u00e4hlen Sie einen Service</h3>'),
    ('<button class="course-nav-link" onclick="showSection(\'one-on-one\')">Instant 1-on-1 Online Session</button>',
     '<button class="course-nav-link" onclick="showSection(\'one-on-one\')">Sofortiges 1-zu-1-Online-Gespr\u00e4ch</button>'),
    ('<button class="course-nav-link" onclick="showSection(\'long-term\')">Long-Term Program (Step-by-Step Growth Plan)</button>',
     '<button class="course-nav-link" onclick="showSection(\'long-term\')">Langzeitprogramm (Stufenplan)</button>'),
    ('<button class="course-nav-link" onclick="showSection(\'booking\')">Book Now</button>',
     '<button class="course-nav-link" onclick="showSection(\'booking\')">Jetzt buchen</button>'),
    ('<div id="select-hint">Please Choose a Service First</div>',
     '<div id="select-hint">Bitte w\u00e4hlen Sie zuerst einen Service</div>'),
    # 一对一
    ('<h2>Instant 1-on-1 Online Session</h2>', '<h2>Sofortiges 1-zu-1-Online-Gespr\u00e4ch</h2>'),
    ('<p style="text-align: center; color: #d9d9d9; font-size: 1.1rem; margin-bottom: 40px;">Any topic goes: track polishing, technical roadblocks, production breakdowns and more</p>',
     '<p style="text-align: center; color: #d9d9d9; font-size: 1.1rem; margin-bottom: 40px;">Keine Tabu-Themen: Track-Feinschliff, technische H\u00fcrden, Produktions-Analysen und mehr</p>'),
    ('<span>1 hour \u00b7 Focused Q&amp;A</span><strong style="color: #fff;">$60</strong>',
     '<span>1 Stunde \u00b7 Gezielte Antworten</span><strong style="color: #fff;">60 \u20ac</strong>'),
    ('<span>2 hours \u00b7 In-Depth Review</span><strong style="color: #fff;">$95</strong>',
     '<span>2 Stunden \u00b7 Vertiefte Analyse</span><strong style="color: #fff;">95 \u20ac</strong>'),
    ('<span>3 hours \u00b7 Full System Customization</span><strong style="color: #fff;">$120</strong>',
     '<span>3 Stunden \u00b7 Systematische Ma\u00dfschneiderung</span><strong style="color: #fff;">120 \u20ac</strong>'),
    # 长期课程
    ('<h2>Long-Term Program (Step-by-Step Growth Plan)</h2>', '<h2>Langzeitprogramm (Stufenplan)</h2>'),
    ('<strong>Student identities are kept strictly confidential. Each course is bound to an independent ID with an ECC digital signature \u2014 progress can be verified on this site with a unique serial number.</strong>',
     '<strong>Die Identit\u00e4t der Teilnehmer wird streng vertraulich behandelt. Jeder Kurs ist an eine unabh\u00e4ngige Nummer mit digitaler ECC-Signatur gebunden \u2014 den Fortschritt k\u00f6nnen Sie auf dieser Website per Seriennummer \u00fcberpr\u00fcfen.</strong>'),
    # 初级
    ('<span class="course-level beginner">Beginner</span>', '<span class="course-level beginner">Einsteiger</span>'),
    ('<h3>Trance Production Fundamentals (Live Group Sessions)</h3>', '<h3>Trance-Produktion Grundlagen (Live-Gruppensessions)</h3>'),
    ('<div class="price-tag small">$220</div>', '<div class="price-tag small">220 \u20ac</div>'),
    ('<strong>Who it\u2019s for:</strong> complete beginners and the simply curious \u2014 anyone who wants to experience the Trance production process firsthand, gain basic arranging skills, and broaden their musical taste.',
     '<strong>F\u00fcr wen:</strong> absolute Anf\u00e4nger und Neugierige \u2014 alle, die den Trance-Produktionsprozess hautnah erleben, grundlegende Arrangement-F\u00e4higkeiten erwerben und ihren musikalischen Horizont erweitern m\u00f6chten.'),
    ('<li><strong>Format:</strong> live small-group sessions (2\u20134 people), relaxed pace, until you\u2019re done</li>',
     '<li><strong>Format:</strong> Live-Kleingruppen (2\u20134 Personen), entspanntes Tempo, bis Sie fertig sind</li>'),
    ('<li><strong>Core content:</strong> a systematic introduction to the Trance style \u2014 take a track from zero to a complete piece, while protecting and nurturing your curiosity.</li>',
     '<li><strong>Kerninhalte:</strong> eine systematische Einf\u00fchrung in den Trance-Stil \u2014 von null bis zum kompletten Track, mit Raum f\u00fcr Ihre Neugier und Ihren Entdeckungsdrang.</li>'),
    ('<strong>Requirements:</strong> basic DAW skills and a pair of entry-level monitoring headphones (confirmed with you before enrollment).',
     '<strong>Voraussetzungen:</strong> grundlegende DAW-Bedienung und ein einfaches Monitoring-Kopfh\u00f6rerpaar (wird vor der Anmeldung mit Ihnen abgekl\u00e4rt).'),
    ('<div class="course-benefit">Graduate benefit: 10% off the next tier\u2019s full course with your certificate; the top-rated final project earns an extra $44 credit, usable on any course.</div>',
     '<div class="course-benefit">Absolventen-Vorteil: 10 % Rabatt auf den Vollkurs der n\u00e4chsten Stufe mit Ihrem Zertifikat; die beste Abschlussarbeit erh\u00e4lt zus\u00e4tzlich einen Gutschein von 44 \u20ac, f\u00fcr jeden Kurs einsetzbar.</div>'),
    # 中级
    ('<span class="course-level intermediate">Intermediate</span>', '<span class="course-level intermediate">Fortgeschrittene</span>'),
    ('<h3>Style Development + Artist Growth Plan (1-on-1)</h3>', '<h3>Stilentwicklung + K\u00fcnstlerentwicklung (1-zu-1)</h3>'),
    ('<div class="price-tag small">$790 (includes six months of guidance)</div>', '<div class="price-tag small">790 \u20ac (inklusive sechs Monaten Betreuung)</div>'),
    ('<strong>Who it\u2019s for:</strong> producers with a foundation who are ready to follow the mentor\u2019s direction, execute consistently and finish the work \u2014 and who want to break through plateaus, develop a personal style, aim for label releases, and build a professional artist profile.',
     '<strong>F\u00fcr wen:</strong> Produzenten mit Grundlagen, die bereit sind, der Mentor-Richtung zu folgen, konsequent umzusetzen und Aufgaben zu Ende zu bringen \u2014 und die Plateaus durchbrechen, einen pers\u00f6nlichen Stil entwickeln, Label-Releases anstreben und ein professionelles K\u00fcnstlerprofil aufbauen m\u00f6chten.'),
    ('<li><strong>Format:</strong> 1-on-1 teaching and guidance + six months of ongoing Q&amp;A (about 20 sessions, tailored to you) + assignment feedback + regular reviews. You may pause 2\u20133 times and must finish within one year (special cases negotiable). A personal digital pass is issued, with course progress verifiable in real time.</li>',
     '<li><strong>Format:</strong> 1-zu-1-Unterricht und Betreuung + sechs Monate laufende Frage-Antwort-Betreuung (ca. 20 Einheiten, individuell angepasst) + Feedback zu Aufgaben + regelm\u00e4\u00dfige Reviews. Pausen sind 2\u20133-mal m\u00f6glich; der Abschluss sollte innerhalb eines Jahres erfolgen (Sonderf\u00e4lle verhandelbar). Ausgestellt wird ein pers\u00f6nlicher digitaler Pass mit jederzeit \u00fcberpr\u00fcfbarem Kursfortschritt.</li>'),
    ('<li><strong>Core content:</strong> develop your own dance music style, build personal aesthetics with guidance, and create a distinctive sonic identity; the fundamentals and practice of mixing and mastering, up to release standard; and a professional production mindset that goes beyond trial-and-error experience.</li>',
     '<li><strong>Kerninhalte:</strong> Entwicklung Ihres eigenen Dancemusic-Stils, Aufbau pers\u00f6nlicher \u00c4sthetik mit Anleitung und eine unverwechselbare Klangidentit\u00e4t; Grundlagen und Praxis von Mixing und Mastering auf Release-Niveau; und eine professionelle Produktions-Denkhaltung, die \u00fcber reine Versuch-und-Irrtum-Erfahrung hinausgeht.</li>'),
    ('<li><strong>Artist development:</strong> self-promotion planning, label-targeting strategy, artist self-management, presentation of your music, and building a sustainable artist image.</li>',
     '<li><strong>K\u00fcnstlerentwicklung:</strong> Planung der Eigenvermarktung, Strategie zur Label-Ansprache, k\u00fcnstlerisches Selbstmanagement, Pr\u00e4sentation Ihrer Musik und Aufbau eines tragf\u00e4higen K\u00fcnstler-Images.</li>'),
    ('<li><strong>Exclusive:</strong> staged assignments with hard criteria to keep quality high; full progress follow-up; and guidance on submitting to labels.</li>',
     '<li><strong>Exklusiv:</strong> gestufte Aufgaben mit klaren Kriterien f\u00fcr konstante Qualit\u00e4t; l\u00fcckenlose Betreuung des Fortschritts; und Begleitung bei Label-Submissions.</li>'),
    ('<strong>Requirements:</strong> proficient DAW operation; open or semi-open monitoring headphones recommended (confirmed before enrollment); an entrance assessment is required to confirm fit.',
     '<strong>Voraussetzungen:</strong> sichere DAW-Bedienung; offene oder halboffene Monitoring-Kopfh\u00f6rer empfohlen (wird vor der Anmeldung abgekl\u00e4rt); vor der Anmeldung ist ein Einstufungstest erforderlich.'),
    ('<div class="course-benefit">Graduates receive a certificate of completion and a personal skills certificate (on request), plus a three-year support plan: an annual collaboration opportunity with the mentor, along with ongoing benefits and discounts.</div>',
     '<div class="course-benefit">Absolventen erhalten ein Abschlusszertifikat und auf Wunsch ein pers\u00f6nliches Kompetenzzertifikat, plus ein dreij\u00e4hriges Betreuungsprogramm: j\u00e4hrlich eine Kollaboration mit dem Mentor sowie laufende Vorteile und Rabatte.</div>'),
    # 高级
    ('<span class="course-level advanced">Advanced</span>', '<span class="course-level advanced">Master</span>'),
    ('<h3>Eonun Trance (Limited)</h3>', '<h3>Eonun Trance (Limitiert)</h3>'),
    ('<div class="price-tag small">Fully booked \u2014 inquire for availability</div>', '<div class="price-tag small">Ausgebucht \u2014 fragen Sie nach freien Kapazit\u00e4ten</div>'),
    ('<strong>Who it\u2019s for:</strong> seasoned producers with years of experience who are after top-tier sound and the latest aesthetic directions, and who want a fundamental breakthrough \u2014 aimed at those pursuing dance music production as a career (not recommended for casual hobbyists).',
     '<strong>F\u00fcr wen:</strong> erfahrene Produzenten mit langj\u00e4hriger Praxis, die h\u00f6chste Klangqualit\u00e4t und die aktuellsten \u00e4sthetischen Entwicklungen suchen und einen grundlegenden Durchbruch anstreben \u2014 gedacht f\u00fcr alle, die Dance-Musik-Produktion beruflich verfolgen (f\u00fcr Gelegenheitshobbyisten nicht empfohlen).'),
    ('<li><strong>Format:</strong> in-depth 1-on-1 mentorship (including private written material) + long-term support + access to the mentor\u2019s network.</li>',
     '<li><strong>Format:</strong> vertiefte 1-zu-1-Betreuung (einschlie\u00dflich privater schriftlicher Unterlagen) + langfristige Begleitung + Zugang zum Netzwerk des Mentors.</li>'),
    ('<li><strong>Core content:</strong> built around a private, unpublished book, the Eonun Trance series deconstructs the underlying logic of groove and the essence of atmosphere generation in Trance from first principles, establishing a systematic framework for groove aesthetics.<br><br>It grounds you in a self-consistent, system-level theory of electroacoustics, works through the coupling mechanisms of multi-effect chains, and delivers a proprietary \u201cprinciple-driven\u201d theory of mixing and production: using underlying mathematical principles as the lever to derive the operating rules behind counterintuitive mixing logic, completing a reverse-engineered, full-structure analysis of Trance works in any style. The goal is a first-principles leap from imitation to reference-free originality \u2014 a sound language and mixing technique matrix that belong to you alone.<br><br>It also covers advanced mastering methodology, the full workflow of international label collaboration and release, and the bridging curriculum that connects onward from the intermediate tier.</li>',
     '<li><strong>Kerninhalte:</strong> Aufbauend auf einem privaten, unver\u00f6ffentlichten Buch dekonstruiert die Eonun-Trance-Reihe die zugrundeliegende Logik des Grooves und das Wesen der Atmosph\u00e4ren-Generierung im Trance von den ersten Prinzipien aus und etabliert einen systematischen Rahmen f\u00fcr Groove-\u00c4sthetik.<br><br>Sie vermittelt eine in sich stimmige elektroakustische Theorie auf Systemebene, arbeitet die Kopplungsmechanismen multipler Effektketten durch und liefert eine eigenst\u00e4ndige, \u201eprinciple-driven\u201c-Theorie von Mixing und Produktion: Mit den zugrundeliegenden mathematischen Prinzipien als Hebel werden die Regeln hinter kontraintuitivem Mixing-Handeln hergeleitet \u2014 eine vollst\u00e4ndige Reverse-Engineering-Analyse von Trance-Werken jedes Stils. Ziel ist ein First-Principles-Sprung von der Imitation zur referenzfreien Originalit\u00e4t \u2014 eine Klangsprache und Mixing-Technik-Matrix, die allein Ihnen geh\u00f6ren.<br><br>Dazu kommen fortgeschrittene Mastering-Methodik, der komplette Ablauf internationaler Label-Kollaboration und -Releases sowie der \u00dcberbr\u00fcckungs-Kurs, der an die Fortgeschrittenen-Stufe anschlie\u00dft.</li>'),
    ('<strong>Requirements:</strong> an established dance music producer \u2014 in both mindset and craft \u2014 assessed comprehensively by the mentor.',
     '<strong>Voraussetzungen:</strong> ein etablierter Dance-Musik-Produzent \u2014 im Denken wie im Handwerk \u2014, der umfassend vom Mentor beurteilt wird.'),
    ('<div class="course-benefit">Graduate privileges: 50% off any course; referral rewards up to $1,400; direct access to the mentor\u2019s resources and long-term support, evolving into a partnership of equals.</div>',
     '<div class="course-benefit">Absolventen-Privilegien: 50 % Rabatt auf jeden Kurs; Empfehlungspr\u00e4mien bis zu 1.400 \u20ac; direkter Zugang zu den Ressourcen des Mentors und langfristige F\u00f6rderung, die in einer Partnerschaft auf Augenh\u00f6he m\u00fcndet.</div>'),
    ('<button type="button" class="discount-btn" onclick="openDiscountModal()">View the Full Discount &amp; Referral System</button>',
     '<button type="button" class="discount-btn" onclick="openDiscountModal()">Das gesamte Rabatt- &amp; Empfehlungssystem ansehen</button>'),
    ('<p class="discount-hint">Tier discounts \u00b7 Alumni referral rewards \u00b7 New student benefits</p>',
     '<p class="discount-hint">Stufen-Rabatte \u00b7 Empfehlungspr\u00e4mien f\u00fcr Absolventen \u00b7 Vorteile f\u00fcr neue Teilnehmer</p>'),
    # 预约
    ('<h2>How to Book &amp; Things to Know</h2>', '<h2>Buchung &amp; Hinweise</h2>'),
    ('<h4>Get in Touch</h4>', '<h4>Erstkontakt</h4>'),
    ('<p>Reach out by email or WeChat with your needs (service tier, questions or goals, and available times). The mentor will assess whether the fit is right.</p>',
     '<p>Schreiben Sie mir per E-Mail oder WeChat mit Ihrem Anliegen (Service-Stufe, Fragen oder Ziele sowie verf\u00fcgbare Zeiten). Der Mentor pr\u00fcft, ob die Zusammenarbeit passt.</p>'),
    ('<h4>Confirm Your Booking</h4>', '<h4>Buchung best\u00e4tigen</h4>'),
    ('<p>Once the time is confirmed, complete payment and send your project files or track excerpts 24\u201372 hours in advance.</p>',
     '<p>Nach der Terminbest\u00e4tigung erfolgt die Zahlung; Projektdateien oder Track-Ausschnitte senden Sie bitte 24\u201372 Stunden im Voraus.</p>'),
    ('<h4>Start Your Session</h4>', '<h4>Betreuungsbeginn</h4>'),
    ('<p>Live interaction via Zoom or Tencent Meeting.</p>', '<p>Live-Austausch via Zoom oder Tencent Meeting.</p>'),
    ('<h3 style="color: #fff; margin-bottom: 20px; text-align: center;">Things to Know</h3>',
     '<h3 style="color: #fff; margin-bottom: 20px; text-align: center;">Wichtige Hinweise</h3>'),
    ('<li style="color: #d9d9d9; padding: 10px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05);">All coaching services do not include producing tracks on your behalf or submitting works for you</li>',
     '<li style="color: #d9d9d9; padding: 10px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05);">Alle Coaching-Leistungen umfassen nicht das Erstellen von Tracks in Ihrem Namen oder das Einreichen von Werken f\u00fcr Sie</li>'),
    ('<li style="color: #d9d9d9; padding: 10px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05);">To reschedule, give at least 12 hours\u2019 notice \u2014 otherwise the session counts as used</li>',
     '<li style="color: #d9d9d9; padding: 10px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05);">Bei Terminverschiebungen gen\u00fcgt eine Vorlaufmeldung von 12 Stunden \u2014 andernfalls gilt die Einheit als verbraucht</li>'),
    ('<li style="color: #d9d9d9; padding: 10px 0;">Long-term programs require an initial review through direct communication before enrollment can be confirmed</li>',
     '<li style="color: #d9d9d9; padding: 10px 0;">Langzeitprogramme erfordern vor der Anmeldung ein Erstgespr\u00e4ch mit Pr\u00fcfung, ob die Voraussetzungen passen</li>'),
    ('<h3>Book Now \u00b7 Start Your Trance Journey</h3>', '<h3>Jetzt buchen \u00b7 Beginnen Sie Ihre Trance-Reise</h3>'),
    ('<p>Book via WeChat or email \u2014 mention \u201cTrance Mentorship + service tier\u201d</p>',
     '<p>Buchung per WeChat oder E-Mail \u2014 mit dem Vermerk \u201eTrance-Mentoring + Service-Stufe\u201c</p>'),
    ('<a href="weixin://" class="cta-button" title="WeChat ID: EonunTrance">Book via WeChat</a>',
     '<a href="weixin://" class="cta-button" title="WeChat ID: EonunTrance">Per WeChat buchen</a>'),
    ('<a href="mailto:eonun.official@gmail.com" class="cta-button">Book via Email</a>',
     '<a href="mailto:eonun.official@gmail.com" class="cta-button">Per E-Mail buchen</a>'),
    ('WeChat: EonunTrance | Email: eonun.official@gmail.com',
     'WeChat: EonunTrance | E-Mail: eonun.official@gmail.com'),
    # 返利弹层
    ('<h2>Discounts &amp; Referrals</h2>', '<h2>Rabatte &amp; Empfehlungspr\u00e4mien</h2>'),
    ('<h3>The Path Upward</h3>', '<h3>Der Weg nach oben</h3>'),
    ('<li>10% off the next tier\u2019s full course after graduation</li>',
     '<li>Nach dem Abschluss 10 % Rabatt auf den Vollkurs der n\u00e4chsten Stufe</li>'),
    ('<li>Masterclass graduates: <strong>50% off any course</strong></li>',
     '<li>Masterclass-Absolventen: <strong>50 % Rabatt auf jeden Kurs</strong></li>'),
    ('<li>Long-term support (intermediate &amp; advanced): 1\u20132 collaboration opportunities with the mentor per year, valid for three years</li>',
     '<li>Langfristige Betreuung (Fortgeschrittene &amp; Master): 1\u20132 Kollaborationen mit dem Mentor pro Jahr, drei Jahre g\u00fcltig</li>'),
    ('<h3>Alumni Referral Rewards</h3>', '<h3>Empfehlungspr\u00e4mien f\u00fcr Absolventen</h3>'),
    ('<li>Rewards: Beginner <strong>$22</strong> / Intermediate <strong>$44</strong> / Master-to-master <strong>$145</strong> (both parties must be masterclass graduates)</li>',
     '<li>Pr\u00e4mien: Einsteiger <strong>20 \u20ac</strong> / Fortgeschrittene <strong>44 \u20ac</strong> / Master-unter-sich <strong>145 \u20ac</strong> (beide Parteien m\u00fcssen Masterclass-Absolventen sein)</li>'),
    ('<li>Referral slots: Beginner 2 / Intermediate 5 (rewards capped at $210) / Master 10 (counted at $145 or $22\u201344 per referral)</li>',
     '<li>Empfehlungs-Kontingente: Einsteiger 2 / Fortgeschrittene 5 (Pr\u00e4mien gedeckelt bei 210 \u20ac) / Master 10 (angerechnet mit 145 \u20ac bzw. 20\u201344 \u20ac pro Empfehlung)</li>'),
    ('<li>Lower tiers may refer upward; the reverse doesn\u2019t apply</li>',
     '<li>Niedrigere Stufen k\u00f6nnen h\u00f6here empfehlen, nicht umgekehrt</li>'),
    ('<li>Payout: half at the midpoint of the course, the remainder at graduation; early withdrawal is prorated by progress</li>',
     '<li>Auszahlung: die H\u00e4lfte zur Kursmitte, der Rest beim Abschluss; vorzeitiger Abbruch wird anteilig nach Fortschritt abgerechnet</li>'),
    ('<li>Rewards are valid for 12 / 24 months and non-transferable</li>',
     '<li>Pr\u00e4mien sind 12 / 24 Monate g\u00fcltig und nicht \u00fcbertragbar</li>'),
    ('<li>If the referred student withdraws and is refunded, the reward is void; any reward already used is deducted from later payments</li>',
     '<li>Erstattet sich die eingeladene Person, verf\u00e4llt die Pr\u00e4mie; bereits genutzte Pr\u00e4mien werden mit sp\u00e4teren Zahlungen verrechnet</li>'),
    ('<h3>New Student Benefits</h3>', '<h3>Vorteile f\u00fcr neue Teilnehmer</h3>'),
    ('<li>After graduating with a certificate, new students enjoy the same alumni benefits, including tier discounts</li>',
     '<li>Nach dem Abschluss mit Zertifikat genie\u00dfen neue Teilnehmer dieselben Absolventen-Vorteile, einschlie\u00dflich der Stufen-Rabatte</li>'),
    # JS 字符串
    ("throw new Error('Slogan file failed to load')", "throw new Error('Slogan-Datei konnte nicht geladen werden')"),
    ("console.log('Failed to load slogans, using fallback text:', error)", "console.log('Slogans konnten nicht geladen werden, Fallback-Text wird verwendet:', error)"),
    ("'Video failed to load, showing fallback background'", "'Video konnte nicht geladen werden, Ersatzhintergrund wird angezeigt'"),
    ("'Video loaded'", "'Video geladen'"),
    ("'Video load timed out, showing fallback background'", "'Video-Ladezeit \u00fcberschritten, Ersatzhintergrund wird angezeigt'"),
]

for old, new in R:
    n = src.count(old)
    if n == 0:
        print('MISS: ' + old[:70]); sys.exit(1)
    src = src.replace(old, new)

leftover = [l.strip()[:80] for l in src.split('\n') if ('$' in l and '${' not in l) or '¥' in l or ('元' in l) and not l.strip().startswith(('/*','*','<!--','//'))]
if leftover:
    print('currency leftover:'); [print(' ', x) for x in leftover]; sys.exit(1)

old_slogan = 'Part of a young life, devoted to the art of Trance'
if src.count(old_slogan) != 2:
    print('slogan count != 2: %d' % src.count(old_slogan)); sys.exit(1)
src = src.replace(old_slogan, 'Ein St\u00fcck eines jungen Lebens, der Kunst des Trance gewidmet')

out = os.path.join(BASE, '..', '..', 'content', 'de', 'instructions.md')
io.open(out, 'w', encoding='utf-8', newline='\n').write(src)
print('written: ' + out)
