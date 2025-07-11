// Toggle sidebar
document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('menu-toggle');
    const wrapper = document.getElementById('wrapper');

    toggleButton.addEventListener('click', () => {
        wrapper.classList.toggle('toggled');
    });
});


 function toggleSubmenu() {
        const submenu = document.querySelector('.submenu');
        submenu.style.display = submenu.style.display === 'none' ? 'block' : 'none';
    }