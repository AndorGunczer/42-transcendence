# Allows App to behave as SPA (Single Page Application) with
#   instructions for frontend to generate html from JSON objects.

#   'reference_name': {
#       'useless_title',
#       'content_for_html_header',
#       'content_for_htmo_main'
#   }

MENU_DATA = {
    'main': {
        'menuTitle': 'Main Menu Buttons',
        'id': 'main',
        'headerItems': [
            {
                'id': 1,
                'type': 'div',
                'class': 'player-info',
                'content': [
                    {
                        'type': 'div',
                        'class': 'a placeholder_player_image'
                    },
                    {
                        'type': 'p',
                        'class': 'u text-white translate',
                        'text': 'logged in as',
                        'key': 'loggedGuest'
                    },
                    {
                        'type': 'p',
                        'class': 'us text-white',
                        'text': 'GUEST',
                    },
                    {
                        'type': 'p',
                        'class': 'w text-white translate',
                        'text': 'wins',
                        'key': 'wins'
                    },
                    {
                        'type': 'p',
                        'class': 'wp text-white',
                        'text': '0',
                    },
                    {
                        'type': 'p',
                        'class': 'l text-white translate',
                        'text': 'losses',
                        'key': 'losses'
                    },
                    {
                        'type': 'p',
                        'class': 'lp text-white',
                        'text': '0',
                    },
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
                'class': 'col-md-12 mt-2 p-3 h-50 w-25 mb-4 rounded bg-secondary bg-gradient text-white translate',
                'text': 'PLAY',
                'onclick': 'load_playMenu()',
                'key': 'play'
            },
            {
                'id': 4,
                'type': 'div',
                'identifier': '',
                'class': 'd-flex flex-row w-25 justify-content-center',
                'content': [
                    {
                        'type': 'button',
                        'text': 'LOGIN',
                        'class': 'col-md-12 mt-2 h-25 w-50 p-3 rounded bg-secondary bg-gradient text-white translate',
                        'identifier': 'button-login',
                        'onclick': 'load_login()',
                        'key': 'login'
                    },
                    {
                        'type': 'button',
                        'text': 'REGISTER',
                        'class': 'col-md-12 mt-2 h-25 w-50 p-3 rounded bg-secondary bg-gradient text-white translate',
                        'identifier': 'button-register',
                        'onclick': 'load_register()',
                        'key': 'register'
                    }
                ]
            }
        ]
    },
    'play_menu': {
        'menuTitle': 'Play Menu Buttons',
        'id': 'play_menu',
        'headerItems': [
            {
                'id': 1,
                'type': 'div',
                'class': 'player-info',
                'content': [
                    {
                        'type': 'div',
                        'class': 'a placeholder_player_image'
                    },
                    {
                        'type': 'p',
                        'class': 'u text-white translate',
                        'text': 'logged in as',
                        'key': 'loggedGuest'
                    },
                    {
                        'type': 'p',
                        'class': 'us text-white',
                        'text': 'GUEST',
                    },
                    {
                        'type': 'p',
                        'class': 'w text-white translate',
                        'text': 'wins',
                        'key': 'wins'
                    },
                    {
                        'type': 'p',
                        'class': 'wp text-white',
                        'text': '0',
                    },
                    {
                        'type': 'p',
                        'class': 'l text-white translate',
                        'text': 'losses',
                        'key': 'losses'
                    },
                    {
                        'type': 'p',
                        'class': 'lp text-white',
                        'text': '0',
                    },
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white translate',
                'text': 'BACK',
                'onclick': 'load_main()',
                'key': 'back'
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
                'class': 'menu-button col-md-12 mt-2 mb-4 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white translate',
                'text': 'SINGLEPLAYER',
                'onclick': 'single_pregame()',
                'key': 'singleplayer'
            },
            {
                'id': 3,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 mb-4 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white translate',
                'text': 'LOCAL',
                'onclick': 'local_pregame()',
                'key': 'local'

            },
            # {
            #     'id': 4,
            #     'type': 'button',
            #     'class': 'menu-button col-md-12 mt-2 mb-4 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
            #     'text': 'ONLINE',
            #     'onclick': 'online_pregame()'
            # },
        ]
    },
    'match_history': {
        'menuTitle': 'Match History',
        'id': 'match_history',
        'headerItems': [
            {
                'id': 1,
                'type': 'div',
                'class': 'player-info',
                'content': [
                    {
                        'type': 'div',
                        'class': 'a placeholder_player_image'
                    },
                    {
                        'type': 'p',
                        'class': 'u text-white translate',
                        'text': 'logged in as',
                        'key': 'loggedGuest'
                    },
                    {
                        'type': 'p',
                        'class': 'us text-white',
                        'text': 'GUEST',
                    },
                    {
                        'type': 'p',
                        'class': 'w text-white translate',
                        'text': 'wins',
                        'key': 'wins'
                    },
                    {
                        'type': 'p',
                        'class': 'wp text-white',
                        'text': '0',
                    },
                    {
                        'type': 'p',
                        'class': 'l text-white translate',
                        'text': 'losses',
                        'key': 'losses'
                    },
                    {
                        'type': 'p',
                        'class': 'lp text-white',
                        'text': '0',
                    },
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white translate',
                'text': 'BACK',
                'onclick': 'load_main()',
                'key': 'back'
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
                'identifier': 'table-container',
                'content': [

                ]
            },
        ]
    },
    'profile': {
        'menuTitle': 'profile',
        'id': 'profile',
        'headerItems': [
            {
                'id': 1,
                'type': 'div',
                'class': 'player-info',
                'content': [
                    {
                        'type': 'div',
                        'class': 'a placeholder_player_image'
                    },
                    {
                        'type': 'p',
                        'class': 'u text-white translate',
                        'text': 'logged in as',
                        'key': 'loggedGuest'
                    },
                    {
                        'type': 'p',
                        'class': 'us text-white',
                        'text': 'GUEST',
                    },
                    {
                        'type': 'p',
                        'class': 'w text-white translate',
                        'text': 'wins',
                        'key': 'wins'
                    },
                    {
                        'type': 'p',
                        'class': 'wp text-white',
                        'text': '0',
                    },
                    {
                        'type': 'p',
                        'class': 'l text-white translate',
                        'text': 'losses',
                        'key': 'losses'
                    },
                    {
                        'type': 'p',
                        'class': 'lp text-white',
                        'text': '0',
                    },
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white translate',
                'text': 'BACK',
                'onclick': 'load_main()',
                'key': 'back'
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
                'class': 'profile_info d-flex flex-column',
                'content': [
                    {
                        'type': 'div',
                        'class': 'placeholder_player_image'
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': 'User: '
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': 'Wins: '
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': 'Losses: '
                    }
                ]
            },
            {
                'id': 2,
                'type': 'div',
                'identifier': 'table-container',
                'content': [

                ]
            },
        ]
    },
    'tournament_main': {
        'menuTitle': 'Tournament Main Menu',
        'id': 'tournament_main',
        'headerItems': [
            {
                'id': 1,
                'type': 'div',
                'class': 'player-info',
                'content': [
                    {
                        'type': 'div',
                        'class': 'a placeholder_player_image'
                    },
                    {
                        'type': 'p',
                        'class': 'u text-white translate',
                        'text': 'logged in as',
                        'key': 'loggedGuest'
                    },
                    {
                        'type': 'p',
                        'class': 'us text-white',
                        'text': 'GUEST',
                    },
                    {
                        'type': 'p',
                        'class': 'w text-white translate',
                        'text': 'wins',
                        'key': 'wins'
                    },
                    {
                        'type': 'p',
                        'class': 'wp text-white',
                        'text': '0',
                    },
                    {
                        'type': 'p',
                        'class': 'l text-white translate',
                        'text': 'losses',
                        'key': 'losses'
                    },
                    {
                        'type': 'p',
                        'class': 'lp text-white',
                        'text': '0',
                    },
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white translate',
                'text': 'BACK',
                'onclick': 'load_main()',
                'key': 'back'
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
                'class': 'tournament_list',
                'content': [
                        # Programmaticaly filled
                    {
                    'type': 'select',
                    'name': 'avatar',
                    'identifier': 'Avatar',
                    'content': [
                        # {
                        #     'type': 'option',
                        #     'value': 'frog_avatar.jpg',
                        #     'text': 'Frog'
                        # },
                        # {
                        #     'type': 'option',
                        #     'value': 'dog_avatar.jpg',
                        #     'text': 'Dog'
                        # },
                        # {
                        #     'type': 'option',
                        #     'value': 'cat_avatar.jpg',
                        #     'text': 'Cat'
                        # },
                    ]
                },
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'text': 'CREATE TOURNAMENT',
                'class': 'menu-button col-md-12 mt-2 mb-4 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white translate',
                'onclick': 'load_tournament_create()',
                'key': 'create tournament'
            },
            {
                'id': 3,
                'type': 'button',
                'text': 'SELECT',
                'class': 'menu-button col-md-12 mt-2 mb-4 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white translate',
                'onclick': 'load_tournament_select()',
                'key': 'select'
            }
        ]
    },
    'tournament_create': {
        'menuTitle': 'Tournament Create Menu',
        'id': 'tournament_create',
        'headerItems': [
            {
                'id': 1,
                'type': 'div',
                'class': 'player-info',
                'content': [
                    {
                        'type': 'div',
                        'class': 'a placeholder_player_image'
                    },
                    {
                        'type': 'p',
                        'class': 'u text-white translate',
                        'text': 'logged in as',
                        'key': 'loggedGuest'
                    },
                    {
                        'type': 'p',
                        'class': 'us text-white',
                        'text': 'GUEST',
                    },
                    {
                        'type': 'p',
                        'class': 'w text-white translate',
                        'text': 'wins',
                        'key': 'wins'
                    },
                    {
                        'type': 'p',
                        'class': 'wp text-white',
                        'text': '0',
                    },
                    {
                        'type': 'p',
                        'class': 'l text-white translate',
                        'text': 'losses',
                        'key': 'losses'
                    },
                    {
                        'type': 'p',
                        'class': 'lp text-white',
                        'text': '0',
                    },
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white translate',
                'text': 'BACK',
                'onclick': 'load_main()',
                'key': 'back'
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
                'type': 'form',
                # 'class': 'tournament_form',
                'identifier': 'tournament_form',
                'content': [
                    {
                        'type': 'div',
                        'class': 'form-group',
                        'content': [
                            {
                                'type': 'label',
                                'for': 'tournament_name',
                                'class': 'text-white translate',
                                'text': 'Tournament Name',
                                'key': 'tournament name'
                            },
                            {
                                'type': 'input',
                                'inputType': 'text',
                                'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                'identifier': 'tournament_name'
                            },
                        ]
                    },
                    {
                        'type': 'div',
                        'class': 'form-group',
                        'content': [
                            {
                                'type': 'label',
                                'for': 'player',
                                'class': 'text-white translate',
                                'text': 'Player Name',
                                'key': 'playername'
                            },
                            {
                                'type': 'input',
                                'inputType': 'text',
                                'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                'identifier': 'player'

                            },
                            {
                                'type': 'input',
                                'inputType': 'button',
                                'class': 'translate',
                                'value': 'Add Player',
                                'key': 'addPlayer',
                                'onclick': 'invokeAddPlayerToTournament(event)'
                            },
                        ]
                    },
                    {
                        'type': 'ul',
                        'identifier': 'tournament_ul',
                        'class': 'text-white',
                        'content': [

                        ],
                    },
                    {
                        'type': 'input',
                        'inputType': 'button',
                        'value': 'Submit',
                        'class': 'menu-button col-md-12 mt-2 w-100 h-25 p-3 rounded bg-secondary bg-gradient text-white translate',
                        'onclick': 'submit_tournament_create(event)',
                        'key': 'submit'
                    }
                ]
            },
        ]
    },
    'tournament_select': {
        'menuTitle': 'Selected Tournament Menu',
        'id': 'tournament_select',
        'headerItems': [
            {
                'id': 1,
                'type': 'div',
                'class': 'player-info',
                'content': [
                    {
                        'type': 'div',
                        'class': 'a placeholder_player_image'
                    },
                    {
                        'type': 'p',
                        'class': 'u text-white translate',
                        'text': 'logged in as',
                        'key': 'loggedGuest'
                    },
                    {
                        'type': 'p',
                        'class': 'us text-white',
                        'text': 'GUEST',
                    },
                    {
                        'type': 'p',
                        'class': 'w text-white translate',
                        'text': 'wins',
                        'key': 'wins'
                    },
                    {
                        'type': 'p',
                        'class': 'wp text-white',
                        'text': '0',
                    },
                    {
                        'type': 'p',
                        'class': 'l text-white translate',
                        'text': 'losses',
                        'key': 'losses'
                    },
                    {
                        'type': 'p',
                        'class': 'lp text-white',
                        'text': '0',
                    },
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white translate',
                'text': 'BACK',
                'onclick': 'load_playMenu()',
                'key': 'back'
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
                'class': 'w-100 d-flex flex-column justify-content-center align-items-center',
                'identifier': 'tournament_form',
                'content': [
                    {
                        'type': 'div',
                        'class': 'participant_list',
                        'content': [

                        ]
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': 'placeholder for next game'
                    },
                    {
                        'type': 'button',
                        'text': 'Play Game',
                        'class': 'menu-items col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                        'onclick': 'load_tournament_localGame()'
                    }
                ]
            },
        ]
    },
    'singleplayer_menu': {
        'menuTitle': 'Singleplayer Menu Buttons',
        'id': 'singleplayer_menu',
        'headerItems': [
            {
                'id': 1,
                'type': 'div',
                'class': 'player-info',
                'content': [
                    {
                        'type': 'div',
                        'class': 'a placeholder_player_image'
                    },
                    {
                        'type': 'p',
                        'class': 'u text-white translate',
                        'text': 'logged in as',
                        'key': 'loggedGuest'
                    },
                    {
                        'type': 'p',
                        'class': 'us text-white',
                        'text': 'GUEST',
                    },
                    {
                        'type': 'p',
                        'class': 'w text-white translate',
                        'text': 'wins',
                        'key': 'wins'
                    },
                    {
                        'type': 'p',
                        'class': 'wp text-white',
                        'text': '0',
                    },
                    {
                        'type': 'p',
                        'class': 'l text-white translate',
                        'text': 'losses',
                        'key': 'losses'
                    },
                    {
                        'type': 'p',
                        'class': 'lp text-white',
                        'text': '0',
                    },
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white translate',
                'text': 'BACK',
                'onclick': 'load_playMenu()',
                'key': 'back'
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
                'class': 'players w-50 d-flex justify-content-center align-items-center',
                'content': [
                    {
                        'type': 'button',
                        'class': 'menu-button col-md-12 mt-2 w-100 h-75 p-3 mt-4 rounded bg-secondary bg-gradient text-white translate',
                        'text': 'PLAY',
                        'onclick': 'load_singleGame()',
                        'key': 'play'
                    }
                ]
            },
        ]
    },
    'online_menu': {
        'menuTitle': 'Online Menu Buttons',
        'id': 'online_menu',
        'headerItems': [
            {
                'id': 1,
                'type': 'div',
                'class': 'player-info',
                'content': [
                    {
                        'type': 'div',
                        'class': 'a placeholder_player_image'
                    },
                    {
                        'type': 'p',
                        'class': 'u text-white translate',
                        'text': 'logged in as',
                        'key': 'loggedGuest'
                    },
                    {
                        'type': 'p',
                        'class': 'us text-white',
                        'text': 'GUEST',
                    },
                    {
                        'type': 'p',
                        'class': 'w text-white translate',
                        'text': 'wins',
                        'key': 'wins'
                    },
                    {
                        'type': 'p',
                        'class': 'wp text-white',
                        'text': '0',
                    },
                    {
                        'type': 'p',
                        'class': 'l text-white translate',
                        'text': 'losses',
                        'key': 'losses'
                    },
                    {
                        'type': 'p',
                        'class': 'lp text-white',
                        'text': '0',
                    },
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white translate',
                'text': 'BACK',
                'onclick': 'load_playMenu()',
                'key': 'back'
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
                                        'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
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
                                        'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                                        'text': 'Submit'
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'type': 'button',
                        'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                        'text': 'play',
                        'onclick': 'load_onlineGame()'
                    }
                ]
            },
        ]
    },
    'local_menu': {
        'menuTitle': 'Local Menu Buttons',
        'id': 'local_menu',
        'headerItems': [
            {
                'id': 1,
                'type': 'div',
                'class': 'player-info',
                'content': [
                    {
                        'type': 'div',
                        'class': 'a placeholder_player_image'
                    },
                    {
                        'type': 'p',
                        'class': 'u text-white translate',
                        'text': 'logged in as',
                        'key': 'loggedGuest'
                    },
                    {
                        'type': 'p',
                        'class': 'us text-white',
                        'text': 'GUEST',
                    },
                    {
                        'type': 'p',
                        'class': 'w text-white translate',
                        'text': 'wins',
                        'key': 'wins'
                    },
                    {
                        'type': 'p',
                        'class': 'wp text-white',
                        'text': '0',
                    },
                    {
                        'type': 'p',
                        'class': 'l text-white translate',
                        'text': 'losses',
                        'key': 'losses'
                    },
                    {
                        'type': 'p',
                        'class': 'lp text-white',
                        'text': '0',
                    },
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white translate',
                'text': 'BACK',
                'onclick': 'load_playMenu()',
                'key': 'back'
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
                                        'class': 'form-group',
                                        'content': [
                                            {
                                                'type': 'label',
                                                'for': 'player1',
                                                'class': 'text-white',
                                                'text': 'player 1: '
                                            },
                                            {
                                                'type': 'input',
                                                'inputType': 'text',
                                                'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                                'identifier': 'player1'
                                            }
                                        ]
                                    },
                                    # {
                                    #     'type': 'div',
                                    #     'content': [
                                    #         {
                                    #             'type': 'label',
                                    #             'for': 'password1',
                                    #             'text': 'password'
                                    #         },
                                    #         {
                                    #             'type': 'input',
                                    #             'inputType': 'password',
                                    #             'identifier': 'password1'
                                    #         }
                                    #     ]
                                    # },
                                    # {
                                    #     'type': 'button',
                                    #     'class': 'menu-button',
                                    #     'text': 'Submit'
                                    # }
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
                                        'class': 'form-group',
                                        'content': [
                                            {
                                                'type': 'label',
                                                'for': 'player2',
                                                'class': 'text-white',
                                                'text': 'player 2: '
                                            },
                                            {
                                                'type': 'input',
                                                'inputType': 'text',
                                                'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                                'identifier': 'player2'
                                            }
                                        ]
                                    },
                                    # {
                                    #     'type': 'div',
                                    #     'content': [
                                    #         {
                                    #             'type': 'label',
                                    #             'for': 'password2',
                                    #             'text': 'password'
                                    #         },
                                    #         {
                                    #             'type': 'input',
                                    #             'inputType': 'password',
                                    #             'identifier': 'password2'
                                    #         }
                                    #     ]
                                    # },
                                    # {
                                    #     'type': 'button',
                                    #     'class': 'menu-button',
                                    #     'text': 'Submit'
                                    # }
                                ]
                            }
                        ]
                    },
                    {
                        'type': 'button',
                        'class': 'menu-button col-md-12 mt-2 w-100 h-25 p-3 rounded bg-secondary bg-gradient text-white translate',
                        'text': 'play',
                        'key': 'play',
                        'onclick': 'submit_local_pregame(event)'
                    }
                ]
            },
        ]
    },
    'register': {
        'menuTitle': 'Local Menu Buttons',
        'id': 'register',
        'headerItems': [
            {
                'id': 1,
                'type': 'div',
                'class': 'player-info',
                'content': [
                    {
                        'type': 'div',
                        'class': 'a placeholder_player_image'
                    },
                    {
                        'type': 'p',
                        'class': 'u text-white translate',
                        'text': 'logged in as',
                        'key': 'loggedGuest'
                    },
                    {
                        'type': 'p',
                        'class': 'us text-white',
                        'text': 'GUEST',
                    },
                    {
                        'type': 'p',
                        'class': 'w text-white translate',
                        'text': 'wins',
                        'key': 'wins'
                    },
                    {
                        'type': 'p',
                        'class': 'wp text-white',
                        'text': '0',
                    },
                    {
                        'type': 'p',
                        'class': 'l text-white translate',
                        'text': 'losses',
                        'key': 'losses'
                    },
                    {
                        'type': 'p',
                        'class': 'lp text-white',
                        'text': '0',
                    },
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white translate',
                'text': 'BACK',
                'onclick': 'load_main()',
                'key': 'back'
            },
            {
                'id': 2,
                'type': 'div',
                'class': 'menu-button'
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
                                'class': 'form-group',
                                'content': [
                                    {
                                        'type': 'label',
                                        'for': 'username',
                                        'class': 'text-white translate',
                                        'text': 'Username ',
                                        'key': 'username '
                                    },
                                    {
                                        'type': 'input',
                                        'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                        'inputType': 'text',
                                        'identifier': 'username',
                                        'name': 'username'
                                    }
                                ]
                            },
                            {
                                'type': 'div',
                                'class': 'form-group',
                                'content': [
                                    {
                                        'type': 'label',
                                        'for': 'password',
                                        'class': 'text-white translate',
                                        'text': 'Password ',
                                        'key': 'password '
                                    },
                                    {
                                        'type': 'input',
                                        'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                        'inputType': 'password',
                                        'identifier': 'password',
                                        'name': 'password'
                                    }
                                ]
                            },
                            {
                                'type': 'div',
                                'class': 'form-group',
                                'content': [
                                    {
                                        'type': 'label',
                                        'for': 'email',
                                        'class': 'text-white translate',
                                        'text': 'Email ',
                                        'key': 'email '
                                    },
                                    {
                                        'type': 'input',
                                        'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                        'inputType': 'text',
                                        'identifier': 'email',
                                        'name': 'email'
                                    }
                                ]
                            },
                            {
                                'type': 'div',
                                'class': 'form-group',
                                'content': [
                                    {
                                        'type': 'label',
                                        'for': 'avatar',
                                        'class': 'text-white translate',
                                        'text': 'Avatar ',
                                        'key': 'avatar '
                                    },
                                    {
                                        'type': 'select',
                                        'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                        'name': 'avatar',
                                        'identifier': 'Avatar',
                                        'content': [

                                        ]
                                    },
                                    {
                                        'type': 'img',
                                        'identifier': 'avatarPic',
                                        'class': 'mb-3',
                                        'src': 'https://localhost/static/images/question_mark.png',
                                    }
                                ]
                            },
                            {
                                'type': 'div',
                                'class': 'form-group',
                                'content': [
                                    {
                                        'type': 'label',
                                        'for': 'fileUpload',
                                        'class': 'text-white translate',
                                        'text': 'Upload Avatar ',
                                        'key': "uploadAvatar "
                                    },
                                    {
                                        'type': 'input',
                                        'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                        'inputType': 'file',
                                        'identifier': 'fileUpload',
                                    },
                                    {
                                        'type': 'button',
                                        'class': 'btn col-md-12 mt-2 w-100 h-10 p-3 m-10 rounded bg-secondary bg-gradient text-white translate',
                                        'text': 'Upload',
                                        'onclick': 'uploadAvatar(event)',
                                        'key': 'upload',
                                    },
                                ]
                            },
                            {
                                'type': 'div',
                                'class': 'form-group d-flex flex-row mt-2',
                                'content': [
                                    {
                                        'type': 'label',
                                        'for': 'twofa',
                                        'class': 'd-block mr-2 text-white translate',
                                        'text': 'Two-Factor Authentication ',
                                        'key': 'Two-Factor Authentication '
                                    },
                                    {
                                        'type': 'input',
                                        'class': 'form-check',
                                        'inputType': 'checkbox',
                                        'identifier': 'twofa',
                                        'name': 'twofa',
                                    }
                                ]
                            },
                            {
                                'type': 'input',
                                'inputType': 'button',
                                'class': 'btn btn-primary col-md-12 mt-2 w-100 h-10 p-3 m-10 rounded bg-secondary bg-gradient text-white translate',
                                'form': 'registration_form',
                                'value': 'SUBMIT',
                                'onclick': 'submit_registration_form(event)',
                                'key': 'submit'
                            }
                        ]
                    }
                ]
            },
        ]
    },
    'login': {
        'menuTitle': 'Local Menu Buttons',
        'id': 'login',
        'headerItems': [
            {
                'id': 1,
                'type': 'div',
                'class': 'player-info',
                'content': [
                    {
                        'type': 'div',
                        'class': 'a placeholder_player_image'
                    },
                    {
                        'type': 'p',
                        'class': 'u text-white translate',
                        'text': 'logged in as',
                        'key': 'loggedGuest'
                    },
                    {
                        'type': 'p',
                        'class': 'us text-white',
                        'text': 'GUEST',
                    },
                    {
                        'type': 'p',
                        'class': 'w text-white translate',
                        'text': 'wins',
                        'key': 'wins'
                    },
                    {
                        'type': 'p',
                        'class': 'wp text-white',
                        'text': '0',
                    },
                    {
                        'type': 'p',
                        'class': 'l text-white translate',
                        'text': 'losses',
                        'key': 'losses'
                    },
                    {
                        'type': 'p',
                        'class': 'lp text-white',
                        'text': '0',
                    },
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white translate',
                'text': 'BACK',
                'onclick': 'load_main()',
                'key': 'back'
            },
            {
                'id': 2,
                'type': 'div',
                'class': 'menu-button'
            }
        ],
        'menuItems': [
            {
                'type': 'form',
                # 'action': '',
                # 'method': 'POST',
                'identifier': 'login_form',
                'content': [
                    {
                        'type': 'div',
                        'class': 'form-group',
                        'content': [
                            {
                                'type': 'label',
                                'for': 'username',
                                'class': 'text-white translate',
                                'text': 'username',
                                'key': 'username'
                            },
                            {
                                'type': 'input',
                                'inputType': 'text',
                                'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                'identifier': 'username',
                                'name': 'username'
                            }
                        ]
                    },
                    {
                        'type': 'div',
                        'class': 'form-group',
                        'content': [
                            {
                                'type': 'label',
                                'for': 'password',
                                'class': 'text-white translate',
                                'text': 'password ',
                                'key': 'password'
                            },
                            {
                                'type': 'input',
                                'inputType': 'password',
                                'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                'identifier': 'password',
                                'name': 'password'
                            }
                        ]
                    },
                    {
                        'type': 'input',
                        'inputType': 'button',
                        'class': 'menu-button col-md-12 mt-2 w-100 p-3 rounded bg-secondary bg-gradient text-white translate',
                        'value': 'SUBMIT',
                        'form': 'login_form',
                        'onclick': 'submit_login_form(event)',
                        'key': 'submit'
                    }
                ]
            },
            {
                'type': 'div',
                'identifier': 'otpPopup',
                'content': [
                    {
                        'type': 'h2',
                        'text': 'Enter OTP',
                    },
                    {
                        'type': 'form',
                        # 'action': '',
                        # 'method': 'POST',
                        'identifier': 'otpForm',
                        'content': [
                            {
                                'type': 'input',
                                'inputType': 'text',
                                'identifier': 'otp',
                                'name': 'top',
                                'placeholder': 'OTP',
                                'required': 'True'
                            },
                            {
                                'type': 'input',
                                'inputType': 'button',
                                'form': 'otpForm',
                                'text': 'Verify',
                                'onclick': 'verify_otp(event)'
                            }
                        ]
                    }
                ]
            }
        ]
    },
    'settings': {
        'menuTitle': 'User Data Change',
        'id': 'settings',
        'headerItems': [
            {
                'id': 1,
                'type': 'div',
                'class': 'player-info',
                'content': [
                    {
                        'type': 'div',
                        'class': 'a placeholder_player_image'
                    },
                    {
                        'type': 'p',
                        'class': 'u text-white translate',
                        'text': 'logged in as',
                        'key': 'loggedGuest'
                    },
                    {
                        'type': 'p',
                        'class': 'us text-white',
                        'text': 'GUEST',
                    },
                    {
                        'type': 'p',
                        'class': 'w text-white translate',
                        'text': 'wins',
                        'key': 'wins'
                    },
                    {
                        'type': 'p',
                        'class': 'wp text-white',
                        'text': '0',
                    },
                    {
                        'type': 'p',
                        'class': 'l text-white translate',
                        'text': 'losses',
                        'key': 'losses'
                    },
                    {
                        'type': 'p',
                        'class': 'lp text-white',
                        'text': '0',
                    },
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white translate',
                'text': 'BACK',
                'onclick': 'load_main()',
                'key': 'back'
            },
            {
                'id': 2,
                'type': 'div',
                'class': 'menu-button'
            }
        ],
        'menuItems': [
            {
                'type': 'form',
                # 'action': '',
                # 'method': 'POST',
                'class': 'd-flex flex-column',
                'identifier': 'settings_form',
                'content': [
                    {
                        'type': 'div',
                        'class': 'form-group',
                        'content': [
                            {
                                'type': 'label',
                                'for': 'username',
                                'class': 'text-white translate',
                                'text': 'Choose New Username ',
                                'key': 'username'
                            },
                            {
                                'type': 'input',
                                'inputType': 'text',
                                'identifier': 'username',
                                'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                'value': ''
                            },
                        ]
                    },
                    {
                        'type': 'div',
                        'class': 'form-group',
                        'content': [
                            {
                                'type': 'label',
                                'for': 'avatar',
                                'class': 'text-white translate',
                                'text': 'Select New Avatar',
                                'key': 'select new avatar'
                            },
                            {
                                'type': 'select',
                                'name': 'avatar',
                                'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                'identifier': 'avatar',
                                'content': [

                                ]
                            },
                        ]
                    },
                    {
                        'type': 'div',
                        'class': 'form-group',
                        'content': [
                            {
                                'type': 'label',
                                'for': 'language',
                                'class': 'text-white translate',
                                'text': 'Select Language',
                                'key': 'select language'
                            },
                            {
                                'type': 'select',
                                'id': 'language',
                                'name': 'language',
                                'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                'identifier': 'language',
                                'content': [
                                    {
                                        'type': 'option',
                                        'value': 'en',
                                        'text': 'English'
                                    },
                                    {
                                        'type': 'option',
                                        'value': 'de',
                                        'text': 'Deutsch'
                                    },
                                    {
                                        'type': 'option',
                                        'value': 'hu',
                                        'text': 'Hungarian'
                                    },
                                ]
                            },
                        ]
                    },
                    {
                        'type': 'button',
                        'class': 'menu-button col-md-12 mt-2 w-100 h-25 p-3 rounded bg-secondary bg-gradient text-white translate',
                        'text': 'DELETE USER STATISTICS',
                        'onclick': 'deleteUserStats(event)',
                        'key': 'delete user statistics'
                    },
                    {
                        'type': 'button',
                        'class': 'menu-button col-md-12 mt-4 w-100 h-25 p-3 rounded bg-secondary bg-gradient text-white translate',
                        'text': 'SAVE',
                        'onclick': 'saveChanges()',
                        'key': 'save'
                    }
                ]
            }
        ]
    },
    'singleplayer_game': {
        'menuTitle': 'Singleplayer Game Window',
        'id': 'singleplayer_game',
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
        'id': 'local_game',
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
        'id': 'online_game',
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