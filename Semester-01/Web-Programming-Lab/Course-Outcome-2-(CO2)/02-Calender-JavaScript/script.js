
function generate() {
    var init_content = "<table BORDER=1 id='calender'><tr><th>SUN</th><th>MON</th><th>TUE</th><th>WED</th><th>THU</th><th>FRI</th><th>SAT</th></tr><tr>"
    var year_get = document.getElementById("year_get").value;
    var month_get = document.getElementById("month_get").value;
    month_get -= 1;
    switch (month_get) {
        case 0: init_content += "<caption><h1>JANUARY<h1></caption>";
            break;
        case 1: init_content += "<caption><h1>FEBRUARY<h1></caption>";
            break;
        case 2: init_content += "<caption><h1>MARCH<h1></caption>";
            break;
        case 3: init_content += "<caption><h1>APRIL<h1></caption>";
            break;
        case 4: init_content += "<caption><h1>MAY<h1></caption>";
            break;
        case 5: init_content += "<caption><h1>JUNE<h1></caption>";
            break;
        case 6: init_content += "<caption><h1>JULY<h1></caption>";
            break;
        case 7: init_content += "<caption><h1>AUGUST<h1></caption>";
            break;
        case 8: init_content += "<caption><h1>SEPTEMBER<h1></caption>";
            break;
        case 9: init_content += "<caption><h1>OBCTOBAR<h1></caption>";
            break;
        case 10: init_content += "<caption><h1>NOVEMBER<h1></caption>";
            break;
        case 11: init_content += "<caption><h1>DECEMBER<h1></caption>";
            break;
    }

    var date = new Date(year_get, month_get);
    var day = date.getDay();
    for (var i = 0; i < day; i++) {
        init_content += "<td></td>";
    }
    while (date.getMonth() == month_get) {
        init_content += "<td>" + date.getDate() + "</td>";
        if (date.getDay() % 7 == 6) {
            init_content += "</tr><tr>";
        }
        date.setDate(date.getDate() + 1);
    }

    while (date.getDay() % 7 != 6 && date.getDay() % 7 != 0) {
        init_content += "<td></td>";
        date.setDate(date.getDate() + 1);
    }

    if (date.getDay() % 7 > 0) {
        init_content += "<td></td></tr>";
    }

    init_content += "</table>"
    document.getElementById("content").innerHTML = init_content;
}