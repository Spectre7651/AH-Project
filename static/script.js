function showhidetutorial(){
    var x = document.getElementById("tutorial");
    if (x.style.display == "none"){
        x.style.display = "block"
    } else {
        x.style.display = "none"
    }
}
function autohidetutorial(){
    if ("{{errormess}}" == "True") {
        alert("Yep I ran")
        var x = document.getElementById("tutorial");
        x.style.display = "none"
    }
}