// 監視対象の要素を指定
const targetElement = document.querySelector('#timeinput-input ');

// MutationObserverのコールバック関数
const observerCallback = (mutationsList, observer) => {
  for (const mutation of mutationsList) {
    if (mutation.type === 'attributes') {
      // 要素の属性が変更された場合の処理
      if (mutation.attributeName === 'value') {
        const newValue = targetElement.value;
        // 値が変更されたらPDFを開く処理を実行
        openPdf(newValue);
      }
    }
  }
};

// MutationObserverを作成
const observer = new MutationObserver(observerCallback);

// 監視を開始
observer.observe(targetElement, { attributes: true });

// PDFを開く処理の例
function openPdf(value) {
  // ここでPDFを開く処理を実装
  // 例: window.open('your-pdf-url?value=' + encodeURIComponent(value));
}