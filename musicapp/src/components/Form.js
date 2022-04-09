import React, { Component } from 'react'

class Form extends Component {
  constructor(props){
    super(props)

    this.state = {
      songname: '',
      comments: '',
      rating:'1'
    }
  }

handleSongChange = (event) => {
   this.setState({
     songname: event.target.value
   })
}
handleCommentsChange = (event) => {
   this.setState({
     comments: event.target.value
   })
}
handleRatingChange = event => {
   this.setState({
     rating: event.target.value
   })
}

handleSubmit = event => {
  alert(`${this.state.username} ${this.state.comments} ${this.state.topic}`)
  event.preventDefault()
}
  render(){
    return(
      <form onSubmit={this.handleSubmit}>
        <div>
          <label>Song</label>
          <input type = 'text'value = {this.state.songname} onChange ={this.handleSongChange} />
        </div>
        <div>
          <label>Comments</label>
          <textarea value = {this.state.comments} onChange = {this.handleCommentsChange}/>
        </div>
        <div>
          <label>Rating</label>
          <select value ={this.state.topic} onChange ={this.handleratingChange}>
          <option value='one'> 1 </option>
          <option value='two'> 2 </option>
          <option value='three'> 3 </option>
          <option value='four'> 4 </option>
          <option value='five'> 5 </option>
          </select>

        </div>
        <button type="submit">Submit</button>
      </form>

    )
  }
}
export default Form
