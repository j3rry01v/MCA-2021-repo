let score = 0;
let name = "";
let counter = 0;
// create our questions
let questions = [
    {
        question: "'OS' computer abbreviation usually means??",
        choiceA: " Order of Significance",
        choiceB: " Open Software",
        choiceC: " Operating System",
        choiceD: "Optical Sensor",
        correct: "C"
    }, {
        question: "'.MPG' extension refers usually to what kind of file?",
        choiceA: " Word Perfect Document file",
        choiceB: "MS Office document",
        choiceC: "Animation/movie file",
        choiceD: " Image file",
        correct: "C"
    }, {
        question: "What is part of a database that holds only one type of information?",
        choiceA: "Report",
        choiceB: "Field",
        choiceC: "Record",
        choiceD: "File",
        correct: "B"
    }, {
        question: "What does SSL stand for?",
        choiceA: "Secure Socket Layer",
        choiceB: "System Socket Layer",
        choiceC: "Superuser System Login",
        choiceD: "Secure System Login",
        correct: "A"
    }
];

let runningQst = 0
const lastQst = questions.length - 1


let renderQuestions = () => {
    let q = questions[runningQst]

    document.getElementById("qst").innerHTML = q.question
    document.getElementById("a").innerHTML = q.choiceA
    document.getElementById("b").innerHTML = q.choiceB
    document.getElementById("c").innerHTML = q.choiceC
    document.getElementById("d").innerHTML = q.choiceD
}

const saveAnswer = () => {

    if (document.querySelector('input[name ="ans"]:checked').value === questions[runningQst].correct) {
        score += 1
    }
    document.getElementById(document.querySelector('input[name ="ans"]:checked').value).checked=false
    if (runningQst < lastQst) {
        runningQst += 1
        renderQuestions()
    }
    else {
        displayScore()
    }

}
const next = () => {
    document.getElementById("info").style.display = "none"
    name += document.getElementById("name").value
    renderQuestions();
    document.getElementById("question").style.display = "block"
}

const displayScore = () => {
    document.getElementById("question").style.display = "none"
    document.getElementById("score_card").style.display = "block"
    const total = Math.round(100 * score / questions.length);
    document.getElementById("name_last").innerHTML = "<p>" + name + "</p>"
    document.getElementById("score").innerHTML = "<p>" + total + "%</p>"

}