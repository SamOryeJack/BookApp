let match_test = 'Chapter 1 this is a test Chapter 2 this is a second test Chapter 3 this is a third test Chapter 4'
let conv_test = match_test.split(' ')
let regex = /Chapter \d+/

let redwall = {
    chapter:[],
    text:[]
}

for (let i = 0; i < conv_test.length; i++){
    debugger
    let chapter = conv_test[i] + ' ' + conv_test[i+1]
    if (regex.test(chapter)){        
        redwall['chapter'].push(chapter)
        conv_test.shift()
        conv_test.shift()
    } else {      
        let temp = ''
        debugger
        for (let j = 0; j < conv_test.length; j++){
            let word = conv_test[j]
            if (word !== 'Chapter'){
                debugger
                temp = temp + ' ' + word
            } else {
                conv_test = conv_test.slice(j)
                i--
                break
            }
        }
        redwall['text'].push(temp)
        i--
    }
}