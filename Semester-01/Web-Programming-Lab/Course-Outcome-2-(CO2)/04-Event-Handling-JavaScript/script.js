let themeChange = () => {
    let body = document.getElementById('body')
    let border = document.getElementById('button')
    const white = "rgb(255, 255, 255)"
    let bgcolor = window.getComputedStyle(body, null).getPropertyValue("background-color")
    if (bgcolor === white) {
        body.style.backgroundColor = "black"
        body.style.color = "white"
        border.style.backgroundColor = "black"
        border.style.border = "1px solid white"
        border.style.color = "white"
        border.innerHTML = "Light Mode"
        border.onmouseover = function () {
            this.style.backgroundColor = "white"
            this.style.color = "black"
        }
    }
    else {
        body.style.backgroundColor = "white"
        body.style.color = "black"
        border.style.backgroundColor = "white"
        border.style.border = "1px solid black"
        border.style.color = "black"
        border.innerHTML = "Dark Mode"
        border.onmouseover = function () {
            this.style.backgroundColor = "black"
            this.style.color = "white"
        }
    }
}