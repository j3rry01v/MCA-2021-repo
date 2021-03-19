const strResult = (e) => {
    let str_inp = document.getElementById('string').value;
    let str_indx = document.getElementById('idx_string').value;
    let str_srh = document.getElementById('srh_string').value
    let str_slice = document.getElementById('slice_string').value
    let str_sub = document.getElementById('sub_string').value
    let str_rpc = document.getElementById('rpc_string').value
    let str_rpc1 = document.getElementById('rpc1_string').value
    let content = "jazzjohn@jazzjohn-Lenovo-V145-15AST:output$ Length of the string is:" + str_inp.length
    content += "<br>The index of the word " + str_indx + " is:" + (parseInt(str_inp.indexOf(str_indx)) + 1)
    content += "<br>The last index of the word " + str_indx + " is:" + (parseInt(str_inp.lastIndexOf(str_indx)) + 1)
    content += "<br>The position of the searched word " + str_srh + " is:" + (parseInt(str_inp.search(str_srh)) + 1)
    content += "<br>The string after slicing  is:" + (str_inp.slice(str_inp.indexOf(str_slice), (str_inp.indexOf(str_slice) + str_slice.length)))
    content += "<br>The substring is:" + (str_inp.substr(str_inp.indexOf(str_sub), str_sub.length))
    content += "<br>The string after replacing with " + str_rpc + " is:" + (str_inp.replace(str_rpc1, str_rpc))
    content += "<br>The upper case form of the string is:" + str_inp.toUpperCase()
    content += "<br>The Lower case form of the string is:" + str_inp.toLowerCase()
    document.getElementById("string_result").innerHTML = content
    document.getElementById("string_result").style.display="block";
}

const mathRresult = () => {
    let num = document.getElementById("num").value
    let pow = document.getElementById("pow").value
    let content = "jazzjohn@jazzjohn-Lenovo-V145-15AST:output$ " + num + " raised to " + pow + " is : " + Math.pow(num, pow)
    content += "<br> Square root of " + num + " is : " + Math.sqrt(num)
    content += "<br> round of " + num + " is: " + Math.round(num)
    content += "<br> ceil value of " + num + " is: " + Math.ceil(num)
    content += "<br> floor value of " + num + " is: " + Math.floor(num)
    content += "<br> absolute value of" + num + " is : " + Math.abs(num)
    content += "<br> sine value of " + num + " is: " + Math.sin(num)
    content += "<br> cosine value of " + num + " is: " + Math.cos(num)
    content += "<br> minimum value in  (0, 150, 30, 20, -8, -200) is : " + Math.min(0, 150, 30, 20, -8, -200);
    content += "<br> maximum value in  (0, 150, 30, 20, -8, -200) is : " + Math.max(0, 150, 30, 20, -8, -200);
    content += "<br> Randome number is : " + Math.random()
    content += "<br> pi value is : " + Math.PI
    document.getElementById("math_result").innerHTML = content
    document.getElementById("math_result").style.display="block";
}