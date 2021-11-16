import React, {useEffect, useState} from 'react';
import {useDispatch, useSelector} from 'react-redux';

// import {getABook} from '../store/books';

import './ReadingPage.css'

import { getAllBooks } from '../store/books';

const ReadingPage = () => {
    const dispatch = useDispatch();
    const books = useSelector(state => state.book)
    useEffect(()=> {
        dispatch(getAllBooks())
    })

    return (
        <div className='container'>
            <div className='head'>
                
            </div>

            <div className='book_body'>

            </div>

            <div className='foot'>

                <div className='stats'>
                    <ul>  
                        <li className='book_select'>'Book:'
                        <select>
                            <option>
                                Redwall
                            </option>
                            <option>
                                Lord Brocktree
                            </option>
                            <option>
                                Martin The Warrior
                            </option>
                        </select>
                        </li>
                        
                        <li>'Chapter:'</li>
                        <li>'Words:'</li>
                    </ul>  
                </div>

                <div className='toolbar'>

                </div>
            </div>
        </div>
    )
}

export default ReadingPage