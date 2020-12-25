// Initialize variables
var player1 = prompt("Ebter your Name you'll be Blue:");
var player1Color = 'rgb(86, 151, 255)';

var player2 = prompt("Ebter your Name you'll be Red:");
var player2Color = 'rgb(237, 45, 73)';

var game_on = true;
var table = $('table tr');

// Just for debug
function reportWin(rowNum, colNum){
    console.log("You won starting at this row,col");
    console.log(rowNum);
    console.log(colNum);
}

// Create function to change color
function changeColor(rowIndex,colIndex,color){
    return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color',color);
}

// return color
function returnColor(rowIndex,colIndex){
    return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color');
}


// Check Bottom
function checkBottom(colIndex){
    var colorReport = returnColor(5,colIndex);
    for (var row =5 ; row > -1 ; row--){
        colorReport = returnColor(row,colIndex)
        if(colorReport ==='rgb(128, 128, 128)'){
            return row;
        }
    }
}

// Color Match Check
function colorMatchCheck(one,two,three,four){
    return (one === two && one === three && one === four && one !== 'rgb(128, 128, 128)' && one !== undefined);
}




// Check Horizontal Wins
function horizontalWinCheck(){
    for(var row =0 ;row <6 ;row++){
        for(var col =0 ; col < 4 ; col++){
            if(colorMatchCheck(returnColor(row,col),returnColor(row,col+1),returnColor(row,col+2), returnColor(row,col+3) )){
                console.log('horizontal');
                reportWin(row,col);
                return true;
            }
            else{
                continue;
            }
        }
    }
}


// Check Vertical Wins
function verticalWinCheck(){
    for(var col =0 ;col <7 ;col++){
        for(var row =0 ; row < 3 ; row++){
            if(colorMatchCheck(returnColor(row,col),returnColor(row+1,col),returnColor(row+2,col), returnColor(row+3,col) )){
                console.log('horizontal');
                reportWin(row,col);
                return true;
            }
            else{
                continue;
            }
        }
    }
}



// // Check Diagonal Wins
// function diagonalWinCheck(){
// }


// Start With player one
var currentPlayer = 1;
var currentName = player1;
var currentColor = player1Color;

$('h3').text(player1 + " it is your turn, pick a column to drop in! ");

$('.board button').on('click',function(){
    var col = $(this).closest('td').index();
    var bottomAvail = checkBottom(col);

    changeColor(bottomAvail,col,currentColor);

    if(horizontalWinCheck() || verticalWinCheck()){
        $('h1').text(currentName + " You have won !!");
        // $('h3').fadeOut();
        // $('h2').fadeOut();
    }

    currentPlayer = currentPlayer * -1;
    
    if(currentPlayer === 1){
        currentName = player1;
        $('h3').text(currentName + " it is your turn.");
        currentColor = player1Color;
    }else{
        currentName = player2;
        $('h3').text(currentName + " it is your turn.");
        currentColor = player2Color;
    }

})
