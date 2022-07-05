<!-- TABLE OF CONTENTS -->
## Table of Contents
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>




<!-- ABOUT THE PROJECT -->
## About The Project

This project is still under active development. The goal is to build an add-on for Slither which will catch all usage of .send() and .transfer() function in a solidity contract. This is a very well-known solidity vulnerability, where the usage of this functions might not be appropriate to transfer ether between contracts. Below there is an example of this vulnerability.

<img src="https://www.researchgate.net/publication/357588999/figure/fig4/AS:1108913911013376@1641397087644/An-Example-of-Gasless-send.png">(https://www.researchgate.net/)

<center><img src="https://www.researchgate.net/publication/357588999/figure/fig4/AS:1108913911013376@1641397087644/An-Example-of-Gasless-send.png"></center>

![Bilby Stampede](https://www.researchgate.net/publication/357588999/figure/fig4/AS:1108913911013376@1641397087644/An-Example-of-Gasless-send.png)

### Built With

* [Slither](https://github.com/crytic/slither)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Install Python3 [https://phoenixnap.com/kb/how-to-install-python-3-ubuntu](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu)
2. Clone the repo and change directory to it
   ```sh
   git clone https://github.com/jcrreis/detect-gasless-send/ && cd detect-gasless-send
   ```
3. Create python virtualenv 
   ```sh
    apt install python3-pip && apt-get install python3-venv && python3 -m venv my_env_project
   ```
4. Install required packages
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

```python3 script.py <solidity file>```
* eg: ```python3 script.py ./GaslessTransfer/gaslesstransfer.sol```

_For more examples, please refer to the [Documentation](https://github.com/jcrreis/detect-gasless-send/)

<p align="right">(<a href="#top">back to top</a>)</p>
