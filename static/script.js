const themeToggle = document.getElementById('themeToggle');
const themeStatus = document.getElementById('themeStatus');

themeToggle.addEventListener('change', function () {
    if (this.checked) {
        document.body.classList.add('dark-theme');
        themeStatus.innerText = 'Chế độ tối';
    } else {
        document.body.classList.remove('dark-theme');
        themeStatus.innerText = 'Chế độ sáng';
    }
});