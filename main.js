const toggleSwitch = document.querySelector('.switch input[type="checkbox"]');

function LightModeToggle(btn) {
    if (btn.target.checked) {
        document.documentElement.setAttribute('data-theme', 'light');
    }
    else {
        document.documentElement.setAttribute('data-theme', 'dark');
    }  
}

toggleSwitch.addEventListener('change', LightModeToggle, false);
