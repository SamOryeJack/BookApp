const GET_BOOKS = "books/GET_BOOKS";

// thunk action - how redux does something, thunk is an action
const getBook = (book) => {
    return {
        type: GET_BOOKS,
        payload: book
    }
}

const initialState = {};


// reducer
const bookReducer = (state=initialState, action) => {
    let newState = {
        ...state
    } 
    switch (action.type) {
        case GET_BOOKS:
            console.log(action.payload, 'this is the payload')
            newState = action.payload
            return newState;
    
        default:
            return state;
    }
}

export const getAllBooks = ()=> async (dispatch) => {
    console.log('before')
    // /books/ does not config to correct place http://127.0.0.1:5000/books/ does
    const response = await fetch('http://127.0.0.1:5000/books/', {
        headers: {
            'Content-Type': 'application/json'
        }
    })
console.log('after');



    if (response.ok){

        const data = await response.json()
        console.log(data, 'data')
        dispatch(getBook(data))
        return response
    }
}

export const getABook = (payload, book_title) => async (dispatch) => {
    const response = await fetch(`/books/${book_title}`, {
        headers: {
            "ContentType": "application/json"
        }
    })

    if (response.ok){
        const data = await response.json()
        dispatch(getBook(data))
        return response
    }
}

export default bookReducer