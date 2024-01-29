function showhidetutorial(){
    var x = document.getElementById("tutorial");
    if (x.style.display == "none"){
        x.style.display = "block"
    } else {
        x.style.display = "none"
    }
}
function autohidetutorial(){
    if (window.location.href.indexOf('caesercipher?') == 1) {
        var x = document.getElementById("tutorial");
        x.style.display = "none"
    }
}