import './App.css';
import Menu from './Menu.js';


function App() {
  return (
    <body>
    <div className="header">
      <header className="header">
        <Menu/>
        <div className="text-top">
          <p>
          Ping-Checker is a modern online tool for website monitoring
          </p>
          <p className="p">
          and  checking availability of hosts, IP addresses.
         </p>
      </div>
      <div className="text-bottom">
        <p>It supports the latest technologies such as localized domain names</p> 
        <p className="p">(both punycode and original formats), hostname IPv6</p>
        <p className="p">  records (also known as AAAA record).</p>
      </div>
      </header>
    </div>
    </body>
  );
};

export default App;
