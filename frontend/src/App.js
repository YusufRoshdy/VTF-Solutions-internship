import React from 'react';
import './App.css';

class Checkbox extends React.Component {
  constructor(props) {
    super(props);
    this.state = {on: false};
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    this.setState(state => ({
      on: !state.on,
    }));
  }

  render() {
    return (
      <button onClick={this.handleClick}>
       <img alt="" src={this.state.on ? 'check-box-icon-png-8.png' : 'check-box-outline-blank-512.png'} />
      </button>
    );
  }
}

async function getData() {
  return [
    {id: 1, hotel: '', price: 200,  room: '231'},
    {id: 2, hotel: '', price: 2531, room: '291'},
    {id: 3, hotel: '', price: 101,  room: '234'},
    {id: 4, hotel: '', price: 2,    room: '131'},
    {id: 5, hotel: '', price: 50,   room: '528'},
    {id: 6, hotel: '', price: 36,   room: '923'},
    {id: 7, hotel: '', price: 624,  room: '783'},
  ];
}

class Cell extends React.Component {
  image() {
    if (this.props.currentPrice === this.props.recommendedPrice)
      return 'blue_check.png';
    else if (this.props.currentPrice < this.props.recommendedPrice)
      return 'green_arrow.png';
    return 'red_arrow.png';
  }

  render() {
    return (
      <div className="cell">
        <div><Checkbox /></div>
        <div>
          <p>{this.props.currentPrice}</p>
          <p>{this.props.recommendedPrice}</p>
        </div>
        <div><img src={this.image()} alt="" /></div>
      </div>
    );
  }
}

class App extends React.Component {
  constructor() {
    super();
    this.state = { recommendedPrice: 0, hotels: [] };
    this.handleInput = this.handleInput.bind(this);
  }

  handleInput(e) {
    this.setState({ recommendedPrice: parseInt(e.target.value, 10) || 0 });
  }

  async componentDidMount() {
    const hotels = await getData();
    this.setState((state) => ({
      hotels,
    }));
  }

  render() {
    return (
      <div style={{textAlign: 'center'}}>
        <input
          type="number"
          min="10"
          max="10000000"
          step="10"
          value={this.state.recommendedPrice}
          onChange={this.handleInput}
        />
        <div className="App">
          {this.state.hotels.map(hotel => (
            <Cell key={hotel.id} currentPrice={hotel.price} recommendedPrice={this.state.recommendedPrice} />
          ))}
        </div>
        <button><img src="apply-now-button.png" alt="Apply" /></button>
      </div>
    );
  }
}

export default App;
