# -*- coding: utf-8 -*-
"""zh-hans -> zh-hant 批量转换：逐页读简体源文件，OpenCC s2t 转换后写入 zh-hant。
价格保持人民币；只转文字，ASCII（路径/lang 码/URL）不受影响。
断言：转换后不得残留常见简体特征字；行数不变；¥ 数量不变。"""
import io, os, sys
from opencc import OpenCC

BASE = os.path.dirname(os.path.abspath(__file__))
cc = OpenCC('s2t')
pages = ['_index.md', 'about.md', 'contact.md', 'instructions.md', 'music-services.md', 'shop.md']

SIMP_MARKERS = ['与', '为', '发', '业', '于', '见', '贝', '车', '门', '问', '间', '现', '学', '经', '约', '级', '际', '围', '员', '头']

for p in pages:
    src_path = os.path.join(BASE, '..', '..', 'content', 'zh-hans', p)
    dst_path = os.path.join(BASE, '..', '..', 'content', 'zh-hant', p)
    src = io.open(src_path, encoding='utf-8').read()
    out = cc.convert(src)
    out = out.replace('/zh-hans/', '/zh-hant/')
    # 行数与货币符号数守恒
    if src.count('\n') != out.count('\n'):
        print('line count changed: ' + p); sys.exit(1)
    if src.count('¥') != out.count('¥'):
        print('yen count changed: ' + p); sys.exit(1)
    # 常见简体特征字残留（整文件扫描，注释/代码里中文注释也应转）
    bad = [m for m in SIMP_MARKERS if m in out]
    if bad:
        print('simplified residue %s in %s' % (bad, p)); sys.exit(1)
    if 'zh-hans' in out.replace('/zh-hans/', '/zh-hant/'):
        print('lang code not switched: ' + p); sys.exit(1)
    io.open(dst_path, 'w', encoding='utf-8', newline='\n').write(out)
    print('converted: ' + p)
