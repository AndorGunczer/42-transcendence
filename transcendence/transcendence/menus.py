MENU_DATA = {
    'main': {
        'menuTitle': 'Main Menu Buttons',
        'headerItems': [
            {
                'id': 1,
                'type': 'p',
                'label': 'logged in as PLACEHOLDER'
            },
            {
                'id': 2,
                'type': 'div'
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
                        'label': 'PONG',
                        'identifier': 'container-logo',
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'label': 'PLAY',
                'action': 'load_playMenu()'
            },
            {
                'id': 3,
                'type': 'button',
                'label': 'TOURNAMENT',
                'action': 'load_tournament()'
            },
            {
                'id': 4,
                'type': 'button',
                'label': 'LEADERBOARD',
                'action': 'load_leaderboard()'
            },
            {
                'id': 5,
                'type': 'div',
                'identifier': '',
                'class': 'button-container',
                'content': [
                    {
                        'type': 'button',
                        'label': 'LOGIN',
                        'class': 'menu-button-05',
                        'identifier': 'button-login',
                        'action': 'load_login()'
                    },
                    {
                        'type': 'button',
                        'label': 'REGISTER',
                        'class': 'menu-button-05',
                        'identifier': 'button-register',
                        'action': 'load_register()'
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
                'type': 'p',
                'label': 'logged in as PLACEHOLDER'
            },
            {
                'id': 2,
                'type': 'button',
                'label': 'BACK',
                'action': 'load_main()'
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
                        'label': 'PONG',
                        'identifier': 'container-logo',
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'label': 'SINGLEPLAYER',
                'action': 'single_pregame()'
            },
            {
                'id': 3,
                'type': 'button',
                'label': 'LOCAL',
                'action': 'local_pregame()'

            },
            {
                'id': 4,
                'type': 'button',
                'label': 'ONLINE',
                'action': 'online_pregame()'
            },
        ]
    },
    'singleplayer_menu': {
        'menuTitle': 'Singleplayer Menu Buttons',
        'headerItems': [
            {
                'id': 1,
                'type': 'p',
                'label': 'logged in as PLACEHOLDER'
            },
            {
                'id': 2,
                'type': 'button',
                'label': 'BACK',
                'action': 'load_playMenu()'
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
                    }
                ]
            },
        ]
    }
}