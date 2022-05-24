
let guessForm = document.getElementById("guess-form")
let feedbackContainer = document.getElementById("feedback-container")
let score = 0;
let correctResponses = [];

class GuessFactory{
    constructor(guess){
        this.guess = guess;
        this.getGuess;
        this.giveFeedback;
        this.addToScore;
        

    }

    async getGuess(passedGuess){
        this.passedGuess = passedGuess;
        feedbackContainer.innerHTML = "";
        this.response = await axios.post(`/guess/${this.passedGuess}`);
        
        
        console.log(this.response.data.result);
        return this.giveFeedback(this.response.data.result,this.passedGuess);

    }

    giveFeedback(result,word){
        this.result = result
        this.word = word
        this.feedbackHeadline = document.createElement("h3");
        if(this.result === 'ok' && correctResponses.indexOf(this.word) !== -1){
            this.feedbackHeadline.innerText = "Word is correct, but has already been entered"
        }
        
        if(this.result === 'ok' && correctResponses.indexOf(this.word) === -1){
            this.feedbackHeadline.innerText = "Success!";
            correctResponses.push(this.word);
            feedbackContainer.append(this.feedbackHeadline);
            return this.addToScore(this.word);
        }
       
        if(this.result === 'not-on-board'){
            this.feedbackHeadline.innerText = "The word is not on the board";
        }
        if(this.result === 'not-word'){
            this.feedbackHeadline.innerText = "That's not a word...";
        }
        feedbackContainer.append(this.feedbackHeadline);
    
    }

    addToScore(word){
        this.word=word;
        console.log(`${this.word} addToScore`);
        console.log(this.word.length);

       
        document.getElementById("score-tally").innerText = "";
        this.toAdd = this.word.length;
        score = score + this.toAdd;
        document.getElementById("score-tally").innerText = `Score is ${score}`;
    
    }

}



async function gameOver(){
    document.getElementById("score-tally").innerText = `Game Over! You scored ${score}`;
    let formElements = guessForm.elements;
    for (var i = 0, len = formElements.length; i < len; ++i) {
        formElements[i].disabled = true;
    }
    await highScoreGamesPlayed()
}




async function highScoreGamesPlayed(){
    let storedScore= score;
    let response = await axios.post('/player-data', { storedScore, })
    console.log(response)

}

setTimeout(gameOver, 60000)

guessForm.addEventListener('submit', createGuessFactory)

async function createGuessFactory(e){
    e.preventDefault();
    
    let passedGuess = document.getElementById("text-guess").value;
    let newGuessFactory = new GuessFactory(passedGuess);
    // console.log(passedGuess);
   await newGuessFactory.getGuess(passedGuess);



}










