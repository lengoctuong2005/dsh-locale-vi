import json
from pathlib import Path

source = Path(__file__).with_name('client.js').read_text(encoding='utf-8')
start = source.index('  const dictionaries = ') + len('  const dictionaries = ')
end = source.index(';\n\n  const pluginDictionaries = ', start)
chat = json.loads(source[start:end])['chat']
expected = {
    'chat.deepDivingFor': 'Đang suy nghĩ sâu trong {duration} ···',
    'chat.loadError': 'Không thể tải lịch sử: {message} ({code})',
    'chat.loadOlder': 'Tải lịch sử cũ hơn',
    'chat.loadingHistory': 'Đang tải lịch sử…',
    'chat.toBottom': 'Về cuối cuộc trò chuyện',
    'chat.turnNavigation.jumpLoad': 'Tải và chuyển đến lượt {turn}',
    'chat.turnNavigation.turn': 'Lượt {turn}',
    'message.stepProcess.sharedPrefix': '',
}
for key, value in expected.items():
    assert chat[key] == value, f'{key}: {chat[key]!r} != {value!r}'
conversation = json.loads(source[start:end])['conversation']
assert conversation['file.retry'] == 'Thử tải lại {name}'
voice = json.loads(source[start:end])['voice-input']
assert voice['preparation.loading'] == 'Đang tải {name}…'
plugin_start = end + len(';\n\n  const pluginDictionaries = ')
plugin_end = source.index(';\n\n  window.__ModuleLoader__', plugin_start)
context = json.loads(source[plugin_start:plugin_end])['dsh-context']
assert context['agents.title'] == 'Mạng lưới tác tử'
assert context['agents.sub'] == 'Ngữ cảnh hiện tại của tác tử này và các tác tử phụ · nhấn vào một nút để mở phiên'
assert context['plugin.settings'] == 'Cài đặt plugin'
assert context['plugin.settingsOpen'] == 'Mở cài đặt plugin'
assert context['block.lines'] == '{n} dòng'
assert context['attach.other'] == 'Nội dung khác'
assert context['settings.deltaBase'] == 'Trình duyệt ngữ cảnh · Mốc so sánh'
assert context['files.sort.count'] == 'Hoạt động nhiều nhất'
assert context['tool.sort.count'] == 'Theo số lần gọi'
assert context['gran.modeHint'] == 'Tổng: thành phần tích lũy; Phần tăng: thay đổi so với yêu cầu trước'
assert context['files.sort.lines'] == 'Theo số dòng'
assert context['files.sort.name'] == 'Theo tên'
assert context['placement.hide'] == 'Ẩn'
models = json.loads(source[start:end])['settings.models']
assert models['addModel'] == 'Thêm mô hình'
assert models['contextWindow'] == 'Cửa sổ ngữ cảnh'
assert models['baseUrlEnvironment'] == 'Cấu hình điểm cuối của nhà cung cấp: {env}'
assert models['keyFallbackMissing'] == 'Không phát hiện biến môi trường. Nhập khóa API hoặc cấu hình {hint} trong môi trường.'
assert models['modelIdRequired'] == 'Cần nhập ID mô hình.'
assert models['customRouteTaken'] == 'ID này đã được một nhà cung cấp sử dụng.'
im = json.loads(source[plugin_start:plugin_end])['dsh-im']
assert im['$locale'] == 'en'
assert im['保存'] == 'Lưu'
assert im['刷新'] == 'Làm mới'
assert im['取消'] == 'Hủy'
plugins = json.loads(source[plugin_start:plugin_end])
bs = plugins['betterSidebar']
assert bs['files'] == 'Tệp'
assert bs['explorer'] == 'Trình khám phá'
assert bs['terminal'] == 'Terminal'
assert bs['subagent'] == 'Quản lý tác vụ'
tl = plugins['thinking-levels']
assert tl['card.title'] == 'Mức độ suy nghĩ'
assert tl['card.level.off'] == 'off — Tắt suy nghĩ (chỉ thủ công, không bao giờ tự chọn)'
assert tl['card.level.minimal'] == 'minimal — Nhỏ nhất (tác vụ rất nhẹ)'
assert tl['card.level.max'] == 'max — Tối đa (tác vụ nặng)'
assert tl['card.takeoverUi'] == 'Tiếp quản UI mô hình'
agency = plugins['agency']
assert agency['button.title'] == 'Triệu hồi chuyên gia'
assert agency['settings.title'] == 'Danh sách chuyên gia'
assert agency['custom.new'] == 'Chuyên gia mới'
assert agency['bundle.recommend.title'] == 'Gợi ý chuyên gia theo nhiệm vụ'
assert agency['engineering-hardware-pcb-designer'] == 'Kỹ sư thiết kế phần cứng PCB'
assert agency['expert.engineering-hardware-pcb-designer'] == 'Kỹ sư thiết kế phần cứng PCB'
assert agency['engineering-web-scraping-specialist'] == 'Chuyên gia thu thập & cào dữ liệu Web'
assert agency['expert.engineering-web-scraping-specialist'] == 'Chuyên gia thu thập & cào dữ liệu Web'
cm = plugins['config-manager']
assert cm['section.label'] == 'Sao lưu & Di chuyển'
assert cm['section.settings'] == 'Cài đặt'
assert cm['backupSchedule.title'] == 'Sao lưu toàn bộ theo lịch'
assert cm['nav.sync'] == 'Đồng bộ'
fr = plugins['file-review']
assert fr['settings.title'] == 'Xem lại tệp'
assert fr['produced.summary'] == 'Tệp đã chỉnh sửa'
assert fr['review.layout'] == 'Bố cục diff'
assert fr['produced.undo'] == 'Hoàn tác'
assert fr['produced.redo'] == 'Áp dụng lại'
rewind = plugins['rewind']
assert rewind['button.title'] == 'Tua lại'
assert rewind['button.aria'] == 'Tua lại về tin nhắn này'
assert rewind['popover.chat'] == 'Chỉ tua lại cuộc trò chuyện'
assert rewind['popover.both'] == 'Tua lại cuộc trò chuyện và tệp'
assert rewind['popover.confirm'] == 'Xác nhận tua lại'
tb = plugins['task-board']
assert tb['new.section.attachments'] == 'Tệp đính kèm'
tb_gh = plugins['task-board-github']
assert tb_gh['settings.title'] == 'Đồng bộ GitHub Issues'
gg = plugins['git-graph']
assert gg['branch.create'] == 'Tạo và chuyển sang nhánh mới…'
ops = plugins['dshOps']
assert ops['customPreset'] == 'Preset tùy chỉnh'
ds = plugins['settings.dreamSkin']
assert ds['skin.mist'] == 'Sáng trong thuần khiết'
dfy = plugins['personaDafeiyu']
assert dfy['personaNameDafeiyu'] == 'Đại Phì Ngư (Cá Mập Ú)'
btw = plugins['michengai.btw']
assert btw['selection.ask'] == 'Hỏi bên lề (BTW) đoạn này'
tk = plugins['dsh-plugin-toolkit']
assert tk['tabTitle'] == 'Bác sĩ Plugin'
fs = plugins['web-search-free']
assert fs['searchEngine'] == 'Công cụ tìm kiếm'
trending = plugins['dsh-github-trending']
assert trending['section.title'] == 'Xu hướng GitHub (GitHub Trending)'
auto = json.loads(source[start:end])['dsh-automation']
assert auto['tab'] == 'Nhiệm vụ định kỳ'
print(f'{len(expected)} chat translations, upload retry, voice loading and plugin labels verified')
