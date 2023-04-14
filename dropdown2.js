document.getElementById("options").addEventListener("change", function () {
    var selectedOption = this.value;
    var textarea = document.getElementById("textarea");
    var commentButton = document.getElementById("comment-button");
    if (selectedOption) {
        textarea.style.display = "block";
        commentButton.style.display = "block";
    } else {
        textarea.style.display = "none";
        commentButton.style.display = "none";
    }
});