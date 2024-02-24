# Hangman Game... Now available in your browser!
 
This is a continuation of my previous project https://github.com/SergioPinilla04/Ahorcado. I highly recommend taking a glance at it before diving into this web version of the program.

In order to transform the Hangman game we already have into a web interface, we will use the module CGI for Python.

## Contents

1. [Preparation](#preparation)
2. [The Game](#the-game)
3. [Contributions](#contributions)
4. [License](#license)

## Preparation

First of all, we need to configure our web server to "read" CGI interfaces. In my case it will be Apache, but in any case, we need to edit the configuration file located in Apache24>conf>httpd.conf (on Windows).

![image](https://github.com/SergioPinilla04/Ahorcado_web/assets/113448338/a9f5c97a-9b19-4f59-846d-744c530e30e1)
> [!TIP]
> I left my configuration file on this repository in the case you have any problem.

![image](https://github.com/SergioPinilla04/Ahorcado_web/assets/113448338/4fd1250f-3476-4739-8030-a19af519d56f)

![image](https://github.com/SergioPinilla04/Ahorcado_web/assets/113448338/26bb1c5a-3c83-4c1a-838f-e8591bcdff40)

![image](https://github.com/SergioPinilla04/Ahorcado_web/assets/113448338/6ceb50cb-1266-4dc7-b27d-17315aed644b)

> [!IMPORTANT]
> Make sure to restart Apache after doing any changes on its configuration file!

Now we can add the Python files of the Hangman game into the folder Apache24/cgi-bin:

![image](https://github.com/SergioPinilla04/Ahorcado_web/assets/113448338/78554608-03b9-4a92-86b7-ba22b2416107)

> [!NOTE]
> The database is the same as the one of the previous version of the game.

## The Game

### Sign-up and sing-in

To access the game, we need to search [localhost/cgi-bin-index.py](localhost/cgi-bin-index.py) in our favourite browser. Here we will access the sign-in page:

![image](https://github.com/SergioPinilla04/Ahorcado_web/assets/113448338/d3609090-8591-4409-82c0-5033961507a8)

But first, we need to register ourselves into the data base trhough the link "[Regístrate](localhost/cgi-bin/registro.py)".

![image](https://github.com/SergioPinilla04/Ahorcado_web/assets/113448338/1548b5d6-f899-4ccc-863e-c6c295e0ec1a)

![image](https://github.com/SergioPinilla04/Ahorcado_web/assets/113448338/ff50d740-9828-433d-baf6-057233c6ae8b)

The user has been added to our database:

![image](https://github.com/SergioPinilla04/Ahorcado_web/assets/113448338/ce470aca-828b-40bb-98b3-e02080cae291)

Now we can sign-in into our game with this new user and access the main manu:

![image](https://github.com/SergioPinilla04/Ahorcado_web/assets/113448338/2674192a-c640-48ee-98b9-e54b7fccbaed)

### Parts of the Main Menu

1. If we access the "cuenta" link, we will be able to modify or even delet our account:

![image](https://github.com/SergioPinilla04/Ahorcado_web/assets/113448338/27add44d-3efb-4cd5-95cf-3545ca093f80)

> [!WARNING]
> On this version of the game, the change of the password and the delete of the account are nor working properly.

2. On the "Palabras del Ahorcado" link, we will access another menu, where will be able to choose between:

![image](https://github.com/SergioPinilla04/Ahorcado_web/assets/113448338/4a2a2329-91e7-445a-8c85-5e550a6a7628)

   - **Añadir una palabra al Ahorcado**: where we will be able to add a word into the game:
     
![image](https://github.com/SergioPinilla04/Ahorcado_web/assets/113448338/60be5405-9071-4140-a024-697a18beeefa)

![image](https://github.com/SergioPinilla04/Ahorcado_web/assets/113448338/b8a9d0fe-1c44-4763-b88d-83f46f996119)

This new word has been added into our database:

![image](https://github.com/SergioPinilla04/Ahorcado_web/assets/113448338/676cdc37-26cc-44c5-bfbd-dcdd9c495d66)

   - **Palabras del Ahorcado**: where we can see the words that have been added into the database:

![image](https://github.com/SergioPinilla04/Ahorcado_web/assets/113448338/ea0292e6-592e-4220-a310-689845caf629)

   - **Borrar una palabra del Ahorcado**: you will be able to delete any word.

![image](https://github.com/SergioPinilla04/Ahorcado_web/assets/113448338/26e27004-84e6-4e66-a6ac-c37559b42e6b)

![image](https://github.com/SergioPinilla04/Ahorcado_web/assets/113448338/bb470d29-da97-469e-a5c5-721c72fd3585)

The word has been deleted fon the database:

![image](https://github.com/SergioPinilla04/Ahorcado_web/assets/113448338/5427b0e8-a748-47ec-9704-d20cc2711f34)

3. Back on the main menu, the "Jugar" link takes us to the game, where a random word of the database is selected and we will try and guess word by word:

![image](https://github.com/SergioPinilla04/Ahorcado_web/assets/113448338/1aac0c3e-5c60-4c95-aedf-dcbcb7022c50)

![image](https://github.com/SergioPinilla04/Ahorcado_web/assets/113448338/95b08434-8c78-4e63-ace0-888d15002273)

The database will register the details of the attempts:

![image](https://github.com/SergioPinilla04/Ahorcado_web/assets/113448338/fc47b401-adff-491f-93cf-ef1706c57faa)

> [!WARNING]
> In this version, the game is not working properly yet.

## Contributions

Feel free to contribute to the development of the game. You can open issues to report bugs or suggest new features.

## License

This work is licensed under CC BY-NC-SA 4.0. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/
