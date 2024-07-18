# desktop-pet
A framework for creating highly customizable desktop pets, or running the ones I've created. Currently only supported on Windows.

## Running Pets
Support for creating an executable to be added. For now, the program is run through `__main__.py`

### Default Pets
#### Testpet 
![testpet2](https://github.com/user-attachments/assets/49421a67-e346-4632-b81e-406fb9c40484)
![testpet](https://github.com/user-attachments/assets/5f811699-e831-4f15-a853-71e2c6b395f1)
![testpet3](https://github.com/user-attachments/assets/5ec9cabe-2e81-4c2a-aa7e-384bfb6de7d1)

Testpet is a base example which can be copied and used as reference. Testpet supports being dragged and dropped, 'eating' files by moving them to the recycling bin, and switching between idle and asleep states.

## Adding Pets
To make modifications, clone this repository and install Python >= 3.9.5.  
Install requirements into a virtual environment within the repository:  
```
>python<version> -m venv venv  
>venv\Scripts\activate   
>pip install -r requirements.txt
```

Check out [desktop-pet/pets](https://github.com/crawsoir/desktop-pet/tree/main/desktop-pet/pets) for examples. Tkinter is not required for your pet, however the included tools are dependent on it.

### Testing
TODO: add github automation and testing
