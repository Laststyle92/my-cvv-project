JavaScript
document.addEventListener('DOMContentLoaded', () => {
    console.log('JavaScript успешно подключен и работает в Django!');

    const alertBtn = document.getElementById('demo-btn');
    if (alertBtn) {
        alertBtn.addEventListener('click', () => {
            alert('Привет! Файл main.js из папки static/js работает корректно.');
        });
    }
});