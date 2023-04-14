document.getElementById("paragraph").style.display = "none";
document.getElementById("options").addEventListener("change", function () {
    var selectedOption = this.value;
    var paragraph = document.getElementById("paragraph");
    if (selectedOption === "option1") {
        paragraph.style.display = "block";
    } else if (selectedOption === "option2") {
        paragraph.style.display = "none";
    }
});
