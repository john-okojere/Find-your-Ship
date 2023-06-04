const open = document.getElementById("open");
const close = document.getElementById("close");
const nav = document.getElementById("nav");
const nav_item = document.getElementById("nav_item");

function close_nav() {
    nav.style.height = "10vh";
    nav.style.position = "relative";
    close.style.display = "none"
    open.style.display = "contents"
    nav.style.background="none";
    nav_item.style.display ="none";
}

function open_nav() {
    nav.style.background="rgba(0, 0, 0, 0.949)";
    nav.style.height = "100%";
    nav.style.position = "fixed";
    close.style.display = "contents"
    open.style.display = "none"
    nav_item.style.display ="flex";
}
