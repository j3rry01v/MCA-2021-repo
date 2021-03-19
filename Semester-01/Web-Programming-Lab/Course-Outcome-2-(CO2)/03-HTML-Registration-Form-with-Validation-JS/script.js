const validate = () => {
    let name = document.getElementById('name').value
    let pass = document.getElementById('pass').value
    let cpass = document.getElementById('cpass').value
    let age = document.getElementById('age').value
    let gender = document.querySelector('input[name="gender"]:checked')
    let address = document.getElementById('addr').value
    let phone = document.getElementById('phone').value
    let qualification = document.getElementById('qualification').value
    let nationality = document.getElementById('nationality').value
    let course = document.querySelectorAll('input[name="courses"]:checked')
    let checked_course = Array.prototype.slice.call(course).some(x => x.checked)
    if (name === "") {
        document.getElementById("ename").innerHTML = "*Please enter your name"
        document.getElementById("ename").style.marginTop = "4px"
        document.getElementById("ename").style.display = "block"
        return false;
    }
    if (pass !== cpass) {
        document.getElementById("epass").innerHTML = "*Password doesn't match"
        document.getElementById("epass").style.marginTop = "4px"
        document.getElementById("epass").style.display = "block"
        return false;
    }
    if (pass.length < 6 || pass.length > 12 || !(pass.match(/[0-9]/g)) || !(pass.match(/[a-z]/g)) || !(pass.match(/[A-Z]/g))) {
        document.getElementById("epass").innerHTML = "*password must contain atleast 1 digit , uppercase and lowecase letter"
        document.getElementById("epass").style.marginTop = "4px"
        document.getElementById("epass").style.display = "block"
        return false
    }
    if (!gender || !age || !address || !phone || !qualification || qualification === 'choose' || !nationality || nationality === 'choose' || !checked_course || !gender) {
        document.getElementById("error").innerHTML = "*please enter all details"
        document.getElementById("error").style.display = "block"
        return false
    }
    if (phone.length > 10 || phone.length < 10) {
        document.getElementById("ephone").innerHTML = "*Enter a valid phone number"
        document.getElementById("ephone").style.marginTop = "4px"
        document.getElementById("ephone").style.display = "block"
        return false
    }
    if (!(age.match(/[0-9]/g))) {
        document.getElementById("eage").innerHTML = "*Enter a valid age"
        document.getElementById("eage").style.marginTop = "4px"
        document.getElementById("eage").style.display = "block"
        return false
    }
    else {
        alert("Registration successfull")
    }
}


const remove = () => {
    document.getElementById("ename").style.display = "none"
    document.getElementById("epass").style.display = "none"
    document.getElementById("error").style.display = "none"
}