function speakPost() {
    const contentElement = document.getElementById('post-content');
    if (contentElement) {
        const content = contentElement.innerText;
        const utterance = new SpeechSynthesisUtterance(content);
        utterance.lang = 'en-US';
        utterance.rate = 1;
        speechSynthesis.cancel();
        speechSynthesis.speak(utterance);
    } else {
        console.warn("Post content not found.");
    }
}

function speakText(button) {
    let content = button.getAttribute("data-content"); 
    content = content.replace(/\\u[\dA-F]{4}/gi, ' ').replace(/\s+/g, ' ').trim();
    const utterance = new SpeechSynthesisUtterance(content);
    utterance.lang = 'en-US';
    utterance.rate = 1;
    speechSynthesis.cancel();  
    speechSynthesis.speak(utterance);
}
