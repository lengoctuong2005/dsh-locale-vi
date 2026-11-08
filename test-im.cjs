const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');

const registrations = new Map();
const ctx = {
  effect: (fn) => fn(),
  locale: {
    addLanguage: () => () => {},
    register: (ns, language, dict) => { registrations.set(ns, dict); return () => {}; },
    bind: (ns) => (key) => ns === 'dsh-im' ? `English ${key}` : key,
    subscribe: () => () => {},
  },
};
const window = { __ModuleLoader__: { load: ({ factory }) => factory().apply(ctx) } };
vm.runInNewContext(fs.readFileSync(path.join(__dirname, 'client.js'), 'utf8'), { window, queueMicrotask });
const im = registrations.get('dsh-im');
assert.ok(im);
assert.equal(im['保存'], 'Lưu');
assert.equal(im['$locale'], 'en');
assert.equal(im[' 会话同步设置也会一并删除。'], ' Cài đặt đồng bộ hóa phiên cũng sẽ bị xóa cùng.');
assert.equal(im['AI Office'], 'AI Office');
console.log('IM translated entries retained; untranslated Chinese falls back');
