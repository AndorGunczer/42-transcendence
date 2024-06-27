MENU_DATA = {
    'main': {
        'menuTitle': 'Main Menu Buttons',
        'headerItems': [
            {
                'id': 1,
                'type': 'div',
                'class': 'player-info',
                'content': [
                    {
                        'type': 'div',
                        'class': 'placeholder_player_image'
                    },
                    {
                        'type': 'p',
                        'text': 'logged in as PLACEHOLDER'
                    },
                    {
                        'type': 'p',
                        'text': 'wins'
                    },
                    {
                        'type': 'p',
                        'text': 'losses'
                    }
                ]
            },
            {
                'id': 2,
                'type': 'div',
                'class': 'menu-button'
            }
        ],
        'menuItems': [
            {
                'id': 1,
                'type': 'div',
                'identifier': 'container-logo',
                'content': [
                    {
                        'type': 'h1',
                        'text': 'PONG',
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button',
                'text': 'PLAY',
                'onclick': 'load_playMenu()'
            },
            {
                'id': 3,
                'type': 'button',
                'class': 'menu-button',
                'text': 'TOURNAMENT',
                'onclick': 'load_tournament()'
            },
            {
                'id': 4,
                'type': 'button',
                'class': 'menu-button',
                'text': 'LEADERBOARD',
                'onclick': 'load_leaderboard()'
            },
            {
                'id': 5,
                'type': 'div',
                'identifier': '',
                'class': 'button-container',
                'content': [
                    {
                        'type': 'button',
                        'text': 'LOGIN',
                        'class': 'menu-button-05',
                        'identifier': 'button-login',
                        'onclick': 'load_login()'
                    },
                    {
                        'type': 'button',
                        'text': 'REGISTER',
                        'class': 'menu-button-05',
                        'identifier': 'button-register',
                        'onclick': 'load_register()'
                    }
                ]
            }
        ]
    },
    'play_menu': {
        'menuTitle': 'Play Menu Buttons',
        'headerItems': [
            {
                'id': 1,
                'type': 'div',
                'class': 'player-info',
                'content': [
                    {
                        'type': 'div',
                        'class': 'placeholder_player_image'
                    },
                    {
                        'type': 'p',
                        'text': 'logged in as PLACEHOLDER'
                    },
                    {
                        'type': 'p',
                        'text': 'wins'
                    },
                    {
                        'type': 'p',
                        'text': 'losses'
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button',
                'text': 'BACK',
                'onclick': 'load_main()'
            }
        ],
        'menuItems': [
            {
                'id': 1,
                'type': 'div',
                'identifier': 'container-logo',
                'content': [
                    {
                        'type': 'h1',
                        'text': 'PONG',
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button',
                'text': 'SINGLEPLAYER',
                'onclick': 'single_pregame()'
            },
            {
                'id': 3,
                'type': 'button',
                'class': 'menu-button',
                'text': 'LOCAL',
                'onclick': 'local_pregame()'

            },
            {
                'id': 4,
                'type': 'button',
                'class': 'menu-button',
                'text': 'ONLINE',
                'onclick': 'online_pregame()'
            },
        ]
    },
    'singleplayer_menu': {
        'menuTitle': 'Singleplayer Menu Buttons',
        'headerItems': [
            {
                'id': 1,
                'type': 'div',
                'class': 'player-info',
                'content': [
                    {
                        'type': 'div',
                        'class': 'placeholder_player_image'
                    },
                    {
                        'type': 'p',
                        'text': 'logged in as PLACEHOLDER'
                    },
                    {
                        'type': 'p',
                        'text': 'wins'
                    },
                    {
                        'type': 'p',
                        'text': 'losses'
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button',
                'text': 'BACK',
                'onclick': 'load_playMenu()'
            }
        ],
        'menuItems': [
            {
                'id': 1,
                'type': 'div',
                'class': 'players',
                'content': [
                    {
                        'type': 'div',
                        'class': 'player1',
                        'content': [
                            {
                                'type': 'form',
                                'action': '',
                                'content': [
                                    {
                                        'type': 'div',
                                        'content': [
                                            {
                                                'type': 'label',
                                                'for': 'player1',
                                                'text': 'username'
                                            },
                                            {
                                                'type': 'input',
                                                'inputType': 'text',
                                                'identifier': 'player1'
                                            }
                                        ]
                                    },
                                    {
                                        'type': 'div',
                                        'content': [
                                            {
                                                'type': 'label',
                                                'for': 'password1',
                                                'text': 'password'
                                            },
                                            {
                                                'type': 'input',
                                                'inputType': 'password',
                                                'identifier': 'password1'
                                            }
                                        ]
                                    },
                                    {
                                        'type': 'button',
                                        'class': 'menu-button',
                                        'text': 'Submit'
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'type': 'div',
                        'class': 'player2',
                        'content': [
                            {
                                'type': 'form',
                                'action': '',
                                'content': [
                                    {
                                        'type': 'div',
                                        'content': [
                                            {
                                                'type': 'label',
                                                'for': 'player2',
                                                'text': 'username'
                                            },
                                            {
                                                'type': 'input',
                                                'inputType': 'text',
                                                'identifier': 'player2'
                                            }
                                        ]
                                    },
                                    {
                                        'type': 'div',
                                        'content': [
                                            {
                                                'type': 'label',
                                                'for': 'password2',
                                                'text': 'password'
                                            },
                                            {
                                                'type': 'input',
                                                'inputType': 'password',
                                                'identifier': 'password2'
                                            }
                                        ]
                                    },
                                    {
                                        'type': 'button',
                                        'class': 'menu-button',
                                        'text': 'Submit'
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'type': 'button',
                        'class': 'menu-button',
                        'text': 'play',
                        'onclick': 'load_singleGame()'
                    }
                ]
            },
        ]
    },
    'online_menu': {
        'menuTitle': 'Online Menu Buttons',
        'headerItems': [
            {
                'id': 1,
                'type': 'div',
                'class': 'player-info',
                'content': [
                    {
                        'type': 'div',
                        'class': 'placeholder_player_image'
                    },
                    {
                        'type': 'p',
                        'text': 'logged in as PLACEHOLDER'
                    },
                    {
                        'type': 'p',
                        'text': 'wins'
                    },
                    {
                        'type': 'p',
                        'text': 'losses'
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button',
                'text': 'BACK',
                'onclick': 'load_playMenu()'
            }
        ],
        'menuItems': [
            {
                'id': 1,
                'type': 'div',
                'class': 'players',
                'content': [
                    {
                        'type': 'div',
                        'class': 'player1',
                        'content': [
                            {
                                'type': 'form',
                                'action': '',
                                'content': [
                                    {
                                        'type': 'div',
                                        'content': [
                                            {
                                                'type': 'label',
                                                'for': 'player1',
                                                'text': 'username'
                                            },
                                            {
                                                'type': 'input',
                                                'inputType': 'text',
                                                'identifier': 'player1'
                                            }
                                        ]
                                    },
                                    {
                                        'type': 'div',
                                        'content': [
                                            {
                                                'type': 'label',
                                                'for': 'password1',
                                                'text': 'password'
                                            },
                                            {
                                                'type': 'input',
                                                'inputType': 'password',
                                                'identifier': 'password1'
                                            }
                                        ]
                                    },
                                    {
                                        'type': 'button',
                                        'class': 'menu-button',
                                        'text': 'Submit'
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'type': 'div',
                        'class': 'player2',
                        'content': [
                            {
                                'type': 'form',
                                'action': '',
                                'content': [
                                    {
                                        'type': 'div',
                                        'content': [
                                            {
                                                'type': 'label',
                                                'for': 'player2',
                                                'text': 'username'
                                            },
                                            {
                                                'type': 'input',
                                                'inputType': 'text',
                                                'identifier': 'player2'
                                            }
                                        ]
                                    },
                                    {
                                        'type': 'div',
                                        'content': [
                                            {
                                                'type': 'label',
                                                'for': 'password2',
                                                'text': 'password'
                                            },
                                            {
                                                'type': 'input',
                                                'inputType': 'password',
                                                'identifier': 'password2'
                                            }
                                        ]
                                    },
                                    {
                                        'type': 'button',
                                        'class': 'menu-button',
                                        'text': 'Submit'
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'type': 'button',
                        'class': 'menu-button',
                        'text': 'play',
                        'onclick': 'load_onlineGame()'
                    }
                ]
            },
        ]
    },
    'local_menu': {
        'menuTitle': 'Local Menu Buttons',
        'headerItems': [
            {
                'id': 1,
                'type': 'div',
                'class': 'player-info',
                'content': [
                    {
                        'type': 'div',
                        'class': 'placeholder_player_image'
                    },
                    {
                        'type': 'p',
                        'text': 'logged in as PLACEHOLDER'
                    },
                    {
                        'type': 'p',
                        'text': 'wins'
                    },
                    {
                        'type': 'p',
                        'text': 'losses'
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button',
                'text': 'BACK',
                'onclick': 'load_playMenu()'
            }
        ],
        'menuItems': [
            {
                'id': 1,
                'type': 'div',
                'class': 'players',
                'content': [
                    {
                        'type': 'div',
                        'class': 'player1',
                        'content': [
                            {
                                'type': 'form',
                                'action': '',
                                'content': [
                                    {
                                        'type': 'div',
                                        'content': [
                                            {
                                                'type': 'label',
                                                'for': 'player1',
                                                'text': 'username'
                                            },
                                            {
                                                'type': 'input',
                                                'inputType': 'text',
                                                'identifier': 'player1'
                                            }
                                        ]
                                    },
                                    {
                                        'type': 'div',
                                        'content': [
                                            {
                                                'type': 'label',
                                                'for': 'password1',
                                                'text': 'password'
                                            },
                                            {
                                                'type': 'input',
                                                'inputType': 'password',
                                                'identifier': 'password1'
                                            }
                                        ]
                                    },
                                    {
                                        'type': 'button',
                                        'class': 'menu-button',
                                        'text': 'Submit'
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'type': 'div',
                        'class': 'player2',
                        'content': [
                            {
                                'type': 'form',
                                'action': '',
                                'content': [
                                    {
                                        'type': 'div',
                                        'content': [
                                            {
                                                'type': 'label',
                                                'for': 'player2',
                                                'text': 'username'
                                            },
                                            {
                                                'type': 'input',
                                                'inputType': 'text',
                                                'identifier': 'player2'
                                            }
                                        ]
                                    },
                                    {
                                        'type': 'div',
                                        'content': [
                                            {
                                                'type': 'label',
                                                'for': 'password2',
                                                'text': 'password'
                                            },
                                            {
                                                'type': 'input',
                                                'inputType': 'password',
                                                'identifier': 'password2'
                                            }
                                        ]
                                    },
                                    {
                                        'type': 'button',
                                        'class': 'menu-button',
                                        'text': 'Submit'
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'type': 'button',
                        'class': 'menu-button',
                        'text': 'play',
                        'onclick': 'load_localGame()'
                    }
                ]
            },
        ]
    },
    'register': {
        'menuTitle': 'Local Menu Buttons',
        'headerItems': [
            {
                'id': 1,
                'type': 'div',
                'class': 'player-info',
                'content': [
                    {
                        'type': 'div',
                        'class': 'placeholder_player_image'
                    },
                    {
                        'type': 'p',
                        'text': 'logged in as PLACEHOLDER'
                    },
                    {
                        'type': 'p',
                        'text': 'wins'
                    },
                    {
                        'type': 'p',
                        'text': 'losses'
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button',
                'text': 'BACK',
                'onclick': 'load_main()'
            }
        ],
        'menuItems': [
            {
                'type': 'div',
                'class': 'container',
                'content': [
                    {
                        'type': 'form',
                        # 'action': '/registration_check',
                        # 'method': 'POST',
                        'identifier': 'registration_form',
                        'content': [
                            {
                                'type': 'div',
                                'content': [
                                    {
                                        'type': 'label',
                                        'for': 'username',
                                        'text': 'username: '
                                    },
                                    {
                                        'type': 'input',
                                        'inputType': 'text',
                                        'identifier': 'username',
                                        'name': 'username'
                                    }
                                ]
                            },
                            {
                                'type': 'div',
                                'content': [
                                    {
                                        'type': 'label',
                                        'for': 'password',
                                        'text': 'password: '
                                    },
                                    {
                                        'type': 'input',
                                        'inputType': 'password',
                                        'identifier': 'password',
                                        'name': 'password'
                                    }
                                ]
                            },
                            {
                                'type': 'div',
                                'content': [
                                    {
                                        'type': 'label',
                                        'for': 'avatar',
                                        'text': 'Avatar'
                                    },
                                    {
                                        'type': 'select',
                                        'name': 'avatar',
                                        'identifier': 'Avatar',
                                        'content': [
                                            {
                                                'type': 'option',
                                                'value': 'frog_avatar.jpg',
                                                'text': 'Frog'
                                            },
                                            {
                                                'type': 'option',
                                                'value': 'dog_avatar.jpg',
                                                'text': 'Dog'
                                            },
                                            {
                                                'type': 'option',
                                                'value': 'cat_avatar.jpg',
                                                'text': 'Cat'
                                            },
                                        ]
                                    },
                                    {
                                        'type': 'img',
                                        'identifier': 'avatarPic',
                                        'src': 'https://127.0.0.1:8000/static/images/question_mark.png',
                                    }
                                ]
                            },
                            {
                                'type': 'input',
                                'inputType': 'submit',
                                'form': 'registration_form'
                                # 'onclick': 'registration_check()'
                            }
                        ]
                    }
                ]
            },
        ]
    },
    'login': {
        'menuTitle': 'Local Menu Buttons',
        'headerItems': [
            {
                'id': 1,
                'type': 'div',
                'class': 'player-info',
                'content': [
                    {
                        'type': 'div',
                        'class': 'placeholder_player_image'
                    },
                    {
                        'type': 'p',
                        'text': 'logged in as PLACEHOLDER'
                    },
                    {
                        'type': 'p',
                        'text': 'wins'
                    },
                    {
                        'type': 'p',
                        'text': 'losses'
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button',
                'text': 'BACK',
                'onclick': 'load_main()'
            }
        ],
        'menuItems': [
            {
            'type': 'div',
                'class': 'container',
                'content': [
                    {
                        'type': 'form',
                        # 'action': '',
                        # 'method': 'POST',
                        'identifier': 'login_form',
                        'content': [
                            {
                                'type': 'div',
                                'content': [
                                    {
                                        'type': 'label',
                                        'for': 'username',
                                        'text': 'username: '
                                    },
                                    {
                                        'type': 'input',
                                        'inputType': 'text',
                                        'identifier': 'username',
                                        'name': 'username'
                                    }
                                ]
                            },
                            {
                                'type': 'div',
                                'content': [
                                    {
                                        'type': 'label',
                                        'for': 'password',
                                        'text': 'password: '
                                    },
                                    {
                                        'type': 'input',
                                        'inputType': 'password',
                                        'identifier': 'password',
                                        'name': 'password'
                                    }
                                ]
                            },
                            {
                                'type': 'input',
                                'inputType': 'submit',
                                'form': 'login_form'
                            }
                        ]
                    }
                ]
            },
        ]
    },
    'singleplayer_game': {
        'menuTitle': 'Singleplayer Game Window',
        'headerItems': [

        ],
        'menuItems': [
            {
                'id': 1,
                'type': 'canvas',
                'identifier': 'pongCanvas',
                'width': 800,
                'height': 400
            }
        ]
    },
    'local_game': {
        'menuTitle': 'Local Game Window',
        'headerItems': [

        ],
        'menuItems': [
            {
                'id': 1,
                'type': 'canvas',
                'identifier': 'pongCanvas',
                'width': 800,
                'height': 400
            }
        ]
    },
    'online_game': {
        'menuTitle': 'Online Game Window',
        'headerItems': [

        ],
        'menuItems': [
            {
                'id': 1,
                'type': 'canvas',
                'identifier': 'pongCanvas',
                'width': 800,
                'height': 400
            }
        ]
    }
}