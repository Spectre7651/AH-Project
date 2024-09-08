/* This shows or hides the tutorial div on the cipher page when a button is pressed*/
function showhidetutorial(){
    var x = document.getElementById("tutorial");
    if (x.style.display == "none"){
        x.style.display = "block"
    } else {
        x.style.display = "none"
    }
}