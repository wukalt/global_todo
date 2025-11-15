function toggleSubmenu() {
    const submenu = document.getElementById('submenu');
    submenu.style.display = (submenu.style.display === 'flex') ? 'none' : 'flex';
    submenu.style.flexDirection = 'column';
}