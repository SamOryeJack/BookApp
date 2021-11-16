import React, {useEffect} from 'react';
import {useDispatch, useSelector} from 'react-redux'
import { getAllBooks } from '../../store/books';

import './Library.css'

const Library = () => {
    const dispatch = useDispatch();
    const books = useSelector(state => state.book)
    const allBooks = Object.keys(books)
  
    useEffect(()=> {
        dispatch(getAllBooks())
    },[dispatch])
    return (
        <div className='container'>
            {allBooks.map(book => (
                <div key={book} className='bookCover'>
                    <h2>{book}</h2>
                </div>
            ))}
        </div>
    )
}

export default Library