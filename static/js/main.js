"use strict";
// Nav-Bar Function
const hamburger = document.querySelector('.hamburger');
const icons = [document.querySelector('.bar1'), document.querySelector('.bar2'), document.querySelector('.bar3')];
const navbar = document.querySelector('.mynavbar-links');

let showMenu = false;

function togglemenu () {
    if (!showMenu) {
        for (let i = 0; i < icons.length; i++) {
            const icon = icons[i];
            icon.classList.add('change');
            navbar.classList.add('active');
            
            showMenu = true
        };
    } else {
        for (let i = 0; i < icons.length; i++) {
            const icon = icons[i];
            icon.classList.remove('change');
            navbar.classList.remove('active');
            showMenu = false
        };
    };
};

hamburger.addEventListener('click', togglemenu);

// Dropdown Fuctiom

const dropdownBtn = document.querySelector('.dropdown-icon');
const dropdownMenu = document.querySelector('[data-dropdown-menu]')
const dropdown = document.querySelector('.dropdown');
let showDropdown = false;

function dropdownFunct() {
    if (!showDropdown) {
        dropdownBtn.classList.add('show');
        dropdownMenu.classList.add('show');

        showDropdown = true;

    } else {
        dropdownBtn.classList.remove('show');
        dropdownMenu.classList.remove('show');

        showDropdown = false;
    }
}

dropdown.addEventListener('click', dropdownFunct);
