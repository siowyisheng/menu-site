import React, { useState, useEffect, Fragment } from 'react'
import { render } from 'react-dom'

const App = () => {
  const [items, setItems] = useState([])
  const [categories, setCategories] = useState([])

  useEffect(() => {
    fetch('menu')
      .then(response => response.json())
      .then(data => {
        setItems(data)
        const cat_names = data.map(item => item.category)
        const unique_cats = [...new Set(cat_names)]
        setCategories(unique_cats)
      })
  }, [])

  return (
    <div className="container">
      <div className="row">
        <div className="col-12">
          <div className="mb-4"></div>
          <h1>Nihon No Aji</h1>
          <h3>
            <small className="text-muted">A taste of Japan.</small>
          </h3>
        </div>
        {categories.map(category => (
          <Fragment key={category}>
            <div className="col-12 mt-2">
              <h3>{category}</h3>
            </div>
            {items.map(item => {
              if (item.category == category) {
                return (
                  <div className="col-lg-4 col-md-6 mb-3" key={item.name}>
                    <h5>{item.name}</h5>
                    <p>{item.description}</p>
                    <img src={item.thumbnail}></img>
                  </div>
                )
              }
            })}
          </Fragment>
        ))}
      </div>
    </div>
  )
}

export default App

const container = document.getElementById('app')
render(<App />, container)
