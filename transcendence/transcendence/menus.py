# Allows App to behave as SPA (Single Page Application) with
#   instructions for frontend to generate html from JSON objects.

#   'reference_name': {
#       'useless_title',
#       'content_for_html_header',
#       'content_for_htmo_main'
#   }
from django.utils.translation import gettext as _


MENU_DATA = {
    'main_en': {
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
                        'class': 'text-white',
                        'text': _('logged in as PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('wins')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('losses')
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
                        'text': _('PONG'),
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'col-md-12 mt-2 p-3 h-50 w-25 mb-4 rounded bg-secondary bg-gradient text-white',
                'text': _('PLAY'),
                'onclick': 'load_playMenu()'
            },
            {
                'id': 3,
                'type': 'button',
                'class': 'col-md-12 mt-2 p-3 h-50 w-25 mb-4 rounded bg-secondary bg-gradient text-white',
                'text': _('TOURNAMENT'),
                'onclick': 'load_tournament_main()'
            },
            {
                'id': 4,
                'type': 'button',
                'class': 'col-md-12 mt-2 p-3 h-50 w-25 mb-4 rounded bg-secondary bg-gradient text-white',
                'text': _('LEADERBOARD'),
                'onclick': 'load_leaderboard()'
            },
            {
                'id': 5,
                'type': 'div',
                'identifier': '',
                'class': 'd-flex flex-row w-25 justify-content-center',
                'content': [
                    {
                        'type': 'button',
                        'text': _('LOGIN'),
                        'class': 'col-md-12 mt-2 h-25 w-50 p-3 rounded bg-secondary bg-gradient text-white',
                        'identifier': 'button-login',
                        'onclick': 'load_login()'
                    },
                    {
                        'type': 'button',
                        'text': _('REGISTER'),
                        'class': 'col-md-12 mt-2 h-25 w-50 p-3 rounded bg-secondary bg-gradient text-white',
                        'identifier': 'button-register',
                        'onclick': 'load_register()'
                    }
                ]
            }
        ]
    },
    'main_fr': {
        'menuTitle': 'Boutons du Menu Principal',
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
                        'class': 'text-white',
                        'text': _('connecté en tant que PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('victoires')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('défaites')
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
                        'text': _('PONG'),
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'col-md-12 mt-2 p-3 h-50 w-25 mb-4 rounded bg-secondary bg-gradient text-white',
                'text': _('JOUER'),
                'onclick': 'load_playMenu()'
            },
            {
                'id': 3,
                'type': 'button',
                'class': 'col-md-12 mt-2 p-3 h-50 w-25 mb-4 rounded bg-secondary bg-gradient text-white',
                'text': _('TOURNOI'),
                'onclick': 'load_tournament_main()'
            },
            {
                'id': 4,
                'type': 'button',
                'class': 'col-md-12 mt-2 p-3 h-50 w-25 mb-4 rounded bg-secondary bg-gradient text-white',
                'text': _('CLASSEMENT'),
                'onclick': 'load_leaderboard()'
            },
            {
                'id': 5,
                'type': 'div',
                'identifier': '',
                'class': 'd-flex flex-row w-25 justify-content-center',
                'content': [
                    {
                        'type': 'button',
                        'text': _('CONNEXION'),
                        'class': 'col-md-12 mt-2 h-25 w-50 p-3 rounded bg-secondary bg-gradient text-white',
                        'identifier': 'button-login',
                        'onclick': 'load_login()'
                    },
                    {
                        'type': 'button',
                        'text': _('INSCRIPTION'),
                        'class': 'col-md-12 mt-2 h-25 w-50 p-3 rounded bg-secondary bg-gradient text-white',
                        'identifier': 'button-register',
                        'onclick': 'load_register()'
                    }
                ]
            }
        ]
    },
    'main_es': {
        'menuTitle': 'Botones del Menú Principal',
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
                        'class': 'text-white',
                        'text': _('conectado como PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('victorias')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('derrotas')
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
                        'text': _('PONG'),
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'col-md-12 mt-2 p-3 h-50 w-25 mb-4 rounded bg-secondary bg-gradient text-white',
                'text': _('JUGAR'),
                'onclick': 'load_playMenu()'
            },
            {
                'id': 3,
                'type': 'button',
                'class': 'col-md-12 mt-2 p-3 h-50 w-25 mb-4 rounded bg-secondary bg-gradient text-white',
                'text': _('TORNEO'),
                'onclick': 'load_tournament_main()'
            },
            {
                'id': 4,
                'type': 'button',
                'class': 'col-md-12 mt-2 p-3 h-50 w-25 mb-4 rounded bg-secondary bg-gradient text-white',
                'text': _('TABLA DE CLASIFICACIÓN'),
                'onclick': 'load_leaderboard()'
            },
            {
                'id': 5,
                'type': 'div',
                'identifier': '',
                'class': 'd-flex flex-row w-25 justify-content-center',
                'content': [
                    {
                        'type': 'button',
                        'text': _('INICIAR SESIÓN'),
                        'class': 'col-md-12 mt-2 h-25 w-50 p-3 rounded bg-secondary bg-gradient text-white',
                        'identifier': 'button-login',
                        'onclick': 'load_login()'
                    },
                    {
                        'type': 'button',
                        'text': _('REGISTRARSE'),
                        'class': 'col-md-12 mt-2 h-25 w-50 p-3 rounded bg-secondary bg-gradient text-white',
                        'identifier': 'button-register',
                        'onclick': 'load_register()'
                    }
                ]
            }
        ]
    },
    'play_menu_en': {
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
                        'class': 'text-white',
                        'text': _('logged in as PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('wins')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('losses')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('BACK'),
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
                        'text': _('PONG'),
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 mb-4 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('SINGLEPLAYER'),
                'onclick': 'single_pregame()'
            },
            {
                'id': 3,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 mb-4 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('LOCAL'),
                'onclick': 'local_pregame()'

            },
            {
                'id': 4,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 mb-4 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('ONLINE'),
                'onclick': 'online_pregame()'
            },
        ]
    },
    'play_menu_fr': {
        'menuTitle': 'Boutons du menu de jeu',
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
                        'class': 'text-white',
                        'text': _('connecté en tant que PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('victoires')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('défaites')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('RETOUR'),
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
                        'text': _('PONG'),
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 mb-4 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('SIMPLE JOUEUR'),
                'onclick': 'single_pregame()'
            },
            {
                'id': 3,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 mb-4 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('LOCAL'),
                'onclick': 'local_pregame()'
            },
            {
                'id': 4,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 mb-4 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('EN LIGNE'),
                'onclick': 'online_pregame()'
            },
        ]
    },
    'play_menu_es': {
        'menuTitle': 'Botones del menú de juego',
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
                        'class': 'text-white',
                        'text': _('conectado como PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('victorias')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('derrotas')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('ATRÁS'),
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
                        'text': _('PONG'),
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 mb-4 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('UN JUGADOR'),
                'onclick': 'single_pregame()'
            },
            {
                'id': 3,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 mb-4 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('LOCAL'),
                'onclick': 'local_pregame()'
            },
            {
                'id': 4,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 mb-4 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('EN LÍNEA'),
                'onclick': 'online_pregame()'
            },
        ]
    },
    'tournament_main_en': {
        'menuTitle': 'Tournament Main Menu',
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
                        'class': 'text-white',
                        'text': _('logged in as PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('wins')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('losses')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('BACK'),
                'onclick': 'load_main()'
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
                        #     'text': _('Frog')
                        # },
                        # {
                        #     'type': 'option',
                        #     'value': 'dog_avatar.jpg',
                        #     'text': _('Dog')
                        # },
                        # {
                        #     'type': 'option',
                        #     'value': 'cat_avatar.jpg',
                        #     'text': _('Cat')
                        # },
                    ]
                },
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'text': _('CREATE TOURNAMENT'),
                'class': 'menu-button col-md-12 mt-2 mb-4 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'onclick': 'load_tournament_create()'
            },
            {
                'id': 3,
                'type': 'button',
                'text': _('SELECT'),
                'class': 'menu-button col-md-12 mt-2 mb-4 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'onclick': 'load_tournament_select()'
            }
        ]
    },
        'tournament_create_en': {
        'menuTitle': 'Tournament Create Menu',
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
                        'class': 'text-white',
                        'text': _('logged in as PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('wins')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('losses')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('BACK'),
                'onclick': 'load_main()'
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
                                'class': 'text-white',
                                'text': _('Tournament Name: ')
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
                                'class': 'text-white',
                                'text': _('Player Name: ')
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
                                'value': 'Add Player',
                                'onclick': 'tournament_player_add(event)'
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
                        'class': 'menu-button col-md-12 mt-2 w-100 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                        'onclick': 'submit_tournament_create(event)'
                    }
                ]
            },
        ]
    },
    'tournament_select_en': {
        'menuTitle': 'Selected Tournament Menu',
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
                        'class': 'text-white',
                        'text': _('logged in as PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('wins')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('losses')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('BACK'),
                'onclick': 'load_main()'
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
                        'text': _('placeholder for next game')
                    },
                    {
                        'type': 'button',
                        'text': _('Play Game'),
                        'class': 'menu-items col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                        'onclick': 'load_tournament_localGame()'
                    }
                ]
            },
        ]
    },
    'tournament_main_fr': {
        'menuTitle': 'Menu Principal du Tournoi',
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
                        'class': 'text-white',
                        'text': _('connecté en tant que PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('victoires')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('défaites')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('RETOUR'),
                'onclick': 'load_main()'
            }
        ],
        'menuItems': [
            {
                'id': 1,
                'type': 'div',
                'class': 'tournament_list',
                'content': [
                    {
                        'type': 'select',
                        'name': 'avatar',
                        'identifier': 'Avatar',
                        'content': [
                        ]
                    },
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'text': _('CRÉER UN TOURNOI'),
                'class': 'menu-button col-md-12 mt-2 mb-4 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'onclick': 'load_tournament_create()'
            },
            {
                'id': 3,
                'type': 'button',
                'text': _('SÉLECTIONNER'),
                'class': 'menu-button col-md-12 mt-2 mb-4 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'onclick': 'load_tournament_select()'
            }
        ]
    },

    'tournament_create_fr': {
        'menuTitle': 'Menu de Création de Tournoi',
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
                        'class': 'text-white',
                        'text': _('connecté en tant que PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('victoires')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('défaites')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('RETOUR'),
                'onclick': 'load_main()'
            }
        ],
        'menuItems': [
            {
                'id': 1,
                'type': 'form',
                'identifier': 'tournament_form',
                'content': [
                    {
                        'type': 'div',
                        'class': 'form-group',
                        'content': [
                            {
                                'type': 'label',
                                'for': 'tournament_name',
                                'class': 'text-white',
                                'text': _('Nom du Tournoi : ')
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
                                'class': 'text-white',
                                'text': _('Nom du Joueur : ')
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
                                'value': _('Ajouter Joueur'),
                                'onclick': 'tournament_player_add(event)'
                            },
                        ]
                    },
                    {
                        'type': 'ul',
                        'identifier': 'tournament_ul',
                        'class': 'text-white',
                        'content': []
                    },
                    {
                        'type': 'input',
                        'inputType': 'button',
                        'value': _('Soumettre'),
                        'class': 'menu-button col-md-12 mt-2 w-100 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                        'onclick': 'submit_tournament_create(event)'
                    }
                ]
            },
        ]
    },

    'tournament_select_fr': {
        'menuTitle': 'Menu de Sélection de Tournoi',
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
                        'class': 'text-white',
                        'text': _('connecté en tant que PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('victoires')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('défaites')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('RETOUR'),
                'onclick': 'load_main()'
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
                        'content': []
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('placeholder pour le prochain jeu')
                    },
                    {
                        'type': 'button',
                        'text': _('Jouer au Jeu'),
                        'class': 'menu-items col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                        'onclick': 'load_tournament_localGame()'
                    }
                ]
            },
        ]
    },
    'tournament_main_es': {
    'menuTitle': 'Menú Principal del Torneo',
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
                    'class': 'text-white',
                    'text': _('conectado como PLACEHOLDER')
                },
                {
                    'type': 'p',
                    'class': 'text-white',
                    'text': _('victorias')
                },
                {
                    'type': 'p',
                    'class': 'text-white',
                    'text': _('derrotas')
                }
            ]
        },
        {
            'id': 2,
            'type': 'button',
            'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
            'text': _('ATRÁS'),
            'onclick': 'load_main()'
        }
    ],
    'menuItems': [
        {
            'id': 1,
            'type': 'div',
            'class': 'tournament_list',
            'content': [
                {
                    'type': 'select',
                    'name': 'avatar',
                    'identifier': 'Avatar',
                    'content': [
                    ]
                },
            ]
        },
        {
            'id': 2,
            'type': 'button',
            'text': _('CREAR TORNEO'),
            'class': 'menu-button col-md-12 mt-2 mb-4 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
            'onclick': 'load_tournament_create()'
        },
        {
            'id': 3,
            'type': 'button',
            'text': _('SELECCIONAR'),
            'class': 'menu-button col-md-12 mt-2 mb-4 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
            'onclick': 'load_tournament_select()'
        }
    ]
},

    'tournament_create_es': {
        'menuTitle': 'Menú de Creación del Torneo',
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
                        'class': 'text-white',
                        'text': _('conectado como PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('victorias')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('derrotas')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('ATRÁS'),
                'onclick': 'load_main()'
            }
        ],
        'menuItems': [
            {
                'id': 1,
                'type': 'form',
                'identifier': 'tournament_form',
                'content': [
                    {
                        'type': 'div',
                        'class': 'form-group',
                        'content': [
                            {
                                'type': 'label',
                                'for': 'tournament_name',
                                'class': 'text-white',
                                'text': _('Nombre del Torneo: ')
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
                                'class': 'text-white',
                                'text': _('Nombre del Jugador: ')
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
                                'value': _('Agregar Jugador'),
                                'onclick': 'tournament_player_add(event)'
                            },
                        ]
                    },
                    {
                        'type': 'ul',
                        'identifier': 'tournament_ul',
                        'class': 'text-white',
                        'content': []
                    },
                    {
                        'type': 'input',
                        'inputType': 'button',
                        'value': _('Enviar'),
                        'class': 'menu-button col-md-12 mt-2 w-100 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                        'onclick': 'submit_tournament_create(event)'
                    }
                ]
            },
        ]
    },

    'tournament_select_es': {
        'menuTitle': 'Menú de Selección del Torneo',
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
                        'class': 'text-white',
                        'text': _('conectado como PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('victorias')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('derrotas')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('ATRÁS'),
                'onclick': 'load_main()'
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
                        'content': []
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('placeholder para el próximo juego')
                    },
                    {
                        'type': 'button',
                        'text': _('Jugar Juego'),
                        'class': 'menu-items col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                        'onclick': 'load_tournament_localGame()'
                    }
                ]
            },
        ]
    },
    'singleplayer_menu_en': {
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
                        'class': 'text-white',
                        'text': _('logged in as PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('wins')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('losses')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('BACK'),
                'onclick': 'load_playMenu()'
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
                        'class': 'menu-button col-md-12 mt-2 w-100 h-75 p-3 mt-4 rounded bg-secondary bg-gradient text-white',
                        'text': _('PLAY'),
                        'onclick': 'load_singleGame()'
                    }
                ]
            },
        ]
    },
    'online_menu_en': {
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
                        'class': 'text-white',
                        'text': _('logged in as PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('wins')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('losses')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('BACK'),
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
                                                'text': _('username')
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
                                                'text': _('password')
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
                                        'text': _('Submit')
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
                                                'text': _('username')
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
                                                'text': _('password')
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
                                        'text': _('Submit')
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'type': 'button',
                        'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                        'text': _('play'),
                        'onclick': 'load_onlineGame()'
                    }
                ]
            },
        ]
    },
    'local_menu_en': {
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
                        'class': 'text-white',
                        'text': _('logged in as PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('wins')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('losses')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('BACK'),
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
                                        'class': 'form-group',
                                        'content': [
                                            {
                                                'type': 'label',
                                                'for': 'player1',
                                                'class': 'text-white',
                                                'text': _('player 1: ')
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
                                    #             'text': _('password')
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
                                    #     'text': _('Submit')
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
                                                'text': _('player 2: ')
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
                                    #             'text': _('password')
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
                                    #     'text': _('Submit')
                                    # }
                                ]
                            }
                        ]
                    },
                    {
                        'type': 'button',
                        'class': 'menu-button col-md-12 mt-2 w-100 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                        'text': _('play'),
                        'onclick': 'submit_local_pregame(event)'
                    }
                ]
            },
        ]
    },
    'singleplayer_menu_fr': {
        'menuTitle': 'Boutons du Menu Solo',
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
                        'class': 'text-white',
                        'text': _('connecté en tant que PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('victoires')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('défaites')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('RETOUR'),
                'onclick': 'load_playMenu()'
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
                        'class': 'menu-button col-md-12 mt-2 w-100 h-75 p-3 mt-4 rounded bg-secondary bg-gradient text-white',
                        'text': _('JOUER'),
                        'onclick': 'load_singleGame()'
                    }
                ]
            },
        ]
    },

    'online_menu_fr': {
        'menuTitle': 'Boutons du Menu en Ligne',
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
                        'class': 'text-white',
                        'text': _('connecté en tant que PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('victoires')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('défaites')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('RETOUR'),
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
                                                'text': _('nom d’utilisateur')
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
                                                'text': _('mot de passe')
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
                                        'text': _('Soumettre')
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
                                                'text': _('nom d’utilisateur')
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
                                                'text': _('mot de passe')
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
                                        'text': _('Soumettre')
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'type': 'button',
                        'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                        'text': _('jouer'),
                        'onclick': 'load_onlineGame()'
                    }
                ]
            },
        ]
    },

    'local_menu_fr': {
        'menuTitle': 'Boutons du Menu Local',
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
                        'class': 'text-white',
                        'text': _('connecté en tant que PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('victoires')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('défaites')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('RETOUR'),
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
                                        'class': 'form-group',
                                        'content': [
                                            {
                                                'type': 'label',
                                                'for': 'player1',
                                                'class': 'text-white',
                                                'text': _('joueur 1: ')
                                            },
                                            {
                                                'type': 'input',
                                                'inputType': 'text',
                                                'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                                'identifier': 'player1'
                                            }
                                        ]
                                    },
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
                                                'text': _('joueur 2: ')
                                            },
                                            {
                                                'type': 'input',
                                                'inputType': 'text',
                                                'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                                'identifier': 'player2'
                                            }
                                        ]
                                    },
                                ]
                            }
                        ]
                    },
                    {
                        'type': 'button',
                        'class': 'menu-button col-md-12 mt-2 w-100 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                        'text': _('jouer'),
                        'onclick': 'submit_local_pregame(event)'
                    }
                ]
            },
        ]
    },
    'singleplayer_menu_es': {
        'menuTitle': 'Botones del Menú de un Jugador',
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
                        'class': 'text-white',
                        'text': _('conectado como PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('victorias')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('derrotas')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('ATRÁS'),
                'onclick': 'load_playMenu()'
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
                        'class': 'menu-button col-md-12 mt-2 w-100 h-75 p-3 mt-4 rounded bg-secondary bg-gradient text-white',
                        'text': _('JUGAR'),
                        'onclick': 'load_singleGame()'
                    }
                ]
            },
        ]
    },

    'online_menu_es': {
        'menuTitle': 'Botones del Menú en Línea',
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
                        'class': 'text-white',
                        'text': _('conectado como PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('victorias')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('derrotas')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('ATRÁS'),
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
                                                'text': _('nombre de usuario')
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
                                                'text': _('contraseña')
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
                                        'text': _('Enviar')
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
                                                'text': _('nombre de usuario')
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
                                                'text': _('contraseña')
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
                                        'text': _('Enviar')
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'type': 'button',
                        'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                        'text': _('jugar'),
                        'onclick': 'load_onlineGame()'
                    }
                ]
            },
        ]
    },

    'local_menu_es': {
        'menuTitle': 'Botones del Menú Local',
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
                        'class': 'text-white',
                        'text': _('conectado como PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('victorias')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('derrotas')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('ATRÁS'),
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
                                        'class': 'form-group',
                                        'content': [
                                            {
                                                'type': 'label',
                                                'for': 'player1',
                                                'class': 'text-white',
                                                'text': _('jugador 1: ')
                                            },
                                            {
                                                'type': 'input',
                                                'inputType': 'text',
                                                'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                                'identifier': 'player1'
                                            }
                                        ]
                                    },
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
                                                'text': _('jugador 2: ')
                                            },
                                            {
                                                'type': 'input',
                                                'inputType': 'text',
                                                'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                                'identifier': 'player2'
                                            }
                                        ]
                                    },
                                ]
                            }
                        ]
                    },
                    {
                        'type': 'button',
                        'class': 'menu-button col-md-12 mt-2 w-100 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                        'text': _('jugar'),
                        'onclick': 'submit_local_pregame(event)'
                    }
                ]
            },
        ]
    },

    'register_en': {
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
                        'class': 'text-white',
                        'text': _('logged in as PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('wins')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('losses')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('BACK'),
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
                                'class': 'form-group',
                                'content': [
                                    {
                                        'type': 'label',
                                        'for': 'username',
                                        'class': 'text-white',
                                        'text': _('Username ')
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
                                        'class': 'text-white',
                                        'text': _('Password ')
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
                                        'class': 'text-white',
                                        'text': _('Email ')
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
                                        'class': 'text-white',
                                        'text': _('Avatar ')
                                    },
                                    {
                                        'type': 'select',
                                        'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                        'name': 'avatar',
                                        'identifier': 'Avatar',
                                        'content': [
                                            {
                                                'type': 'option',
                                                'value': 'frog_avatar.jpg',
                                                'text': _('Frog')
                                            },
                                            {
                                                'type': 'option',
                                                'value': 'dog_avatar.jpg',
                                                'text': _('Dog')
                                            },
                                            {
                                                'type': 'option',
                                                'value': 'cat_avatar.jpg',
                                                'text': _('Cat')
                                            },
                                        ]
                                    },
                                    {
                                        'type': 'img',
                                        'identifier': 'avatarPic',
                                        'class': 'mb-3',
                                        'src': 'https://127.0.0.1:8000/static/images/question_mark.png',
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
                                        'class': 'text-white',
                                        'text': _('Upload Avatar '),
                                    },
                                    {
                                        'type': 'input',
                                        'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                        'inputType': 'file',
                                        'identifier': 'fileUpload',
                                    },
                                    {
                                        'type': 'button',
                                        'class': 'btn col-md-12 mt-2 w-100 h-10 p-3 m-10 rounded bg-secondary bg-gradient text-white',
                                        'text': _('Upload'),
                                        'onclick': 'uploadAvatar(event)'
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
                                        'class': 'd-block mr-2 text-white',
                                        'text': _('Two-Factor Authentication ')
                                    },
                                    {
                                        'type': 'input',
                                        'class': 'form-check',
                                        'inputType': 'checkbox',
                                        'identifier': 'twofa',
                                        'name': 'twofa'
                                    }
                                ]
                            },
                            {
                                'type': 'input',
                                'inputType': 'button',
                                'class': 'btn btn-primary col-md-12 mt-2 w-100 h-10 p-3 m-10 rounded bg-secondary bg-gradient text-white',
                                'form': 'registration_form',
                                'value': 'SUBMIT',
                                'onclick': 'submit_registration_form(event)'
                            }
                        ]
                    }
                ]
            },
        ]
    },
    'register_fr': {
        'menuTitle': 'Boutons du Menu d\'Inscription',
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
                        'class': 'text-white',
                        'text': _('connecté en tant que PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('victoires')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('défaites')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('RETOUR'),
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
                                'class': 'form-group',
                                'content': [
                                    {
                                        'type': 'label',
                                        'for': 'username',
                                        'class': 'text-white',
                                        'text': _('Nom d\'utilisateur ')
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
                                        'class': 'text-white',
                                        'text': _('Mot de passe ')
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
                                        'class': 'text-white',
                                        'text': _('E-mail ')
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
                                        'class': 'text-white',
                                        'text': _('Avatar ')
                                    },
                                    {
                                        'type': 'select',
                                        'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                        'name': 'avatar',
                                        'identifier': 'Avatar',
                                        'content': [
                                            {
                                                'type': 'option',
                                                'value': 'frog_avatar.jpg',
                                                'text': _('Grenouille')
                                            },
                                            {
                                                'type': 'option',
                                                'value': 'dog_avatar.jpg',
                                                'text': _('Chien')
                                            },
                                            {
                                                'type': 'option',
                                                'value': 'cat_avatar.jpg',
                                                'text': _('Chat')
                                            },
                                        ]
                                    },
                                    {
                                        'type': 'img',
                                        'identifier': 'avatarPic',
                                        'class': 'mb-3',
                                        'src': 'https://127.0.0.1:8000/static/images/question_mark.png',
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
                                        'class': 'text-white',
                                        'text': _('Télécharger un Avatar ')
                                    },
                                    {
                                        'type': 'input',
                                        'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                        'inputType': 'file',
                                        'identifier': 'fileUpload',
                                    },
                                    {
                                        'type': 'button',
                                        'class': 'btn col-md-12 mt-2 w-100 h-10 p-3 m-10 rounded bg-secondary bg-gradient text-white',
                                        'text': _('Télécharger'),
                                        'onclick': 'uploadAvatar(event)'
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
                                        'class': 'd-block mr-2 text-white',
                                        'text': _('Authentification à Deux Facteurs ')
                                    },
                                    {
                                        'type': 'input',
                                        'class': 'form-check',
                                        'inputType': 'checkbox',
                                        'identifier': 'twofa',
                                        'name': 'twofa'
                                    }
                                ]
                            },
                            {
                                'type': 'input',
                                'inputType': 'button',
                                'class': 'btn btn-primary col-md-12 mt-2 w-100 h-10 p-3 m-10 rounded bg-secondary bg-gradient text-white',
                                'form': 'registration_form',
                                'value': 'SOUMETTRE',
                                'onclick': 'submit_registration_form(event)'
                            }
                        ]
                    }
                ]
            },
        ]
    },
    'register_es': {
        'menuTitle': 'Botones del Menú de Registro',
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
                        'class': 'text-white',
                        'text': _('conectado como PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('victorias')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('derrotas')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('ATRÁS'),
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
                                'class': 'form-group',
                                'content': [
                                    {
                                        'type': 'label',
                                        'for': 'username',
                                        'class': 'text-white',
                                        'text': _('Nombre de usuario ')
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
                                        'class': 'text-white',
                                        'text': _('Contraseña ')
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
                                        'class': 'text-white',
                                        'text': _('Correo electrónico ')
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
                                        'class': 'text-white',
                                        'text': _('Avatar ')
                                    },
                                    {
                                        'type': 'select',
                                        'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                        'name': 'avatar',
                                        'identifier': 'Avatar',
                                        'content': [
                                            {
                                                'type': 'option',
                                                'value': 'frog_avatar.jpg',
                                                'text': _('Rana')
                                            },
                                            {
                                                'type': 'option',
                                                'value': 'dog_avatar.jpg',
                                                'text': _('Perro')
                                            },
                                            {
                                                'type': 'option',
                                                'value': 'cat_avatar.jpg',
                                                'text': _('Gato')
                                            },
                                        ]
                                    },
                                    {
                                        'type': 'img',
                                        'identifier': 'avatarPic',
                                        'class': 'mb-3',
                                        'src': 'https://127.0.0.1:8000/static/images/question_mark.png',
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
                                        'class': 'text-white',
                                        'text': _('Subir Avatar ')
                                    },
                                    {
                                        'type': 'input',
                                        'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                        'inputType': 'file',
                                        'identifier': 'fileUpload',
                                    },
                                    {
                                        'type': 'button',
                                        'class': 'btn col-md-12 mt-2 w-100 h-10 p-3 m-10 rounded bg-secondary bg-gradient text-white',
                                        'text': _('Subir'),
                                        'onclick': 'uploadAvatar(event)'
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
                                        'class': 'd-block mr-2 text-white',
                                        'text': _('Autenticación de Dos Factores ')
                                    },
                                    {
                                        'type': 'input',
                                        'class': 'form-check',
                                        'inputType': 'checkbox',
                                        'identifier': 'twofa',
                                        'name': 'twofa'
                                    }
                                ]
                            },
                            {
                                'type': 'input',
                                'inputType': 'button',
                                'class': 'btn btn-primary col-md-12 mt-2 w-100 h-10 p-3 m-10 rounded bg-secondary bg-gradient text-white',
                                'form': 'registration_form',
                                'value': 'ENVIAR',
                                'onclick': 'submit_registration_form(event)'
                            }
                        ]
                    }
                ]
            },
        ]
    },
    'login_en': {
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
                        'class': 'text-white',
                        'text': _('logged in as PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('wins')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('losses')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('BACK'),
                'onclick': 'load_main()'
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
                                'class': 'text-white',
                                'text': _('username')
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
                                'class': 'text-white',
                                'text': _('password ')
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
                        'class': 'menu-button col-md-12 mt-2 w-100 p-3 rounded bg-secondary bg-gradient text-white',
                        'value': 'SUBMIT',
                        'form': 'login_form',
                        'onclick': 'submit_login_form(event)'
                    }
                ]
            },
            {
                'type': 'div',
                'identifier': 'otpPopup',
                'content': [
                    {
                        'type': 'h2',
                        'text': _('Enter OTP'),
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
                                'text': _('Verify'),
                                'onclick': 'verify_otp(event)'
                            }
                        ]
                    }
                ]
            }
        ]
    },
    'login_fr': {
        'menuTitle': 'Boutons du menu local',
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
                        'class': 'text-white',
                        'text': _('connecté en tant que PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('victoires')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('défaites')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('RETOUR'),
                'onclick': 'load_main()'
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
                                'class': 'text-white',
                                'text': _('nom d\'utilisateur')
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
                                'class': 'text-white',
                                'text': _('mot de passe')
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
                        'class': 'menu-button col-md-12 mt-2 w-100 p-3 rounded bg-secondary bg-gradient text-white',
                        'value': 'SOUMETTRE',
                        'form': 'login_form',
                        'onclick': 'submit_login_form(event)'
                    }
                ]
            },
            {
                'type': 'div',
                'identifier': 'otpPopup',
                'content': [
                    {
                        'type': 'h2',
                        'text': _('Entrez le code OTP'),
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
                                'name': 'otp',
                                'placeholder': 'OTP',
                                'required': 'True'
                            },
                            {
                                'type': 'input',
                                'inputType': 'button',
                                'form': 'otpForm',
                                'text': _('Vérifier'),
                                'onclick': 'verify_otp(event)'
                            }
                        ]
                    }
                ]
            }
        ]
	},
    'login_es': {
        'menuTitle': 'Botones del menú local',
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
                        'class': 'text-white',
                        'text': _('conectado como PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('victorias')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('derrotas')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('ATRÁS'),
                'onclick': 'load_main()'
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
                                'class': 'text-white',
                                'text': _('nombre de usuario')
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
                                'class': 'text-white',
                                'text': _('contraseña')
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
                        'class': 'menu-button col-md-12 mt-2 w-100 p-3 rounded bg-secondary bg-gradient text-white',
                        'value': 'ENVIAR',
                        'form': 'login_form',
                        'onclick': 'submit_login_form(event)'
                    }
                ]
            },
            {
                'type': 'div',
                'identifier': 'otpPopup',
                'content': [
                    {
                        'type': 'h2',
                        'text': _('Ingrese OTP'),
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
                                'name': 'otp',
                                'placeholder': 'OTP',
                                'required': 'True'
                            },
                            {
                                'type': 'input',
                                'inputType': 'button',
                                'form': 'otpForm',
                                'text': _('Verificar'),
                                'onclick': 'verify_otp(event)'
                            }
                        ]
                    }
                ]
            }
        ]
    },
    'settings_en': {
        'menuTitle': 'User Data Change',
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
                        'class': 'text-white',
                        'text': _('logged in as PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('wins')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('losses')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('BACK'),
                'onclick': 'load_main()'
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
                                'class': 'text-white',
                                'text': _('Choose New Username ')
                            },
                            {
                                'type': 'input',
                                'inputType': 'text',
                                'identifier': 'username',
                                'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                'value': 'placeholder'
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
                                'class': 'text-white',
                                'text': _('Select New Avatar')
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
                        'type': 'button',
                        'class': 'menu-button col-md-12 mt-2 w-100 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                        'text': _('Delete User Statistics'),
                        'onclick': 'deleteUserStats(event)',
                    },
                    {
                        'type': 'button',
                        'class': 'menu-button col-md-12 mt-4 w-100 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                        'text': _('Save'),
                        'onclick': 'saveChanges()'
                    }
                ]
            }
        ]
    },
    'settings_fr': {
        'menuTitle': 'Changement des Données Utilisateur',
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
                        'class': 'text-white',
                        'text': _('connecté en tant que PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('victoires')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('défaites')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('RETOUR'),
                'onclick': 'load_main()'
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
                                'class': 'text-white',
                                'text': _('Choisir un nouveau nom d\'utilisateur ')
                            },
                            {
                                'type': 'input',
                                'inputType': 'text',
                                'identifier': 'username',
                                'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                'value': 'placeholder'
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
                                'class': 'text-white',
                                'text': _('Sélectionner un nouvel avatar')
                            },
                            {
                                'type': 'select',
                                'name': 'avatar',
                                'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                'identifier': 'avatar',
                                'content': [
                                    # Ajoutez ici les options pour les avatars
                                ]
                            },
                        ]
                    },
                    {
                        'type': 'button',
                        'class': 'menu-button col-md-12 mt-2 w-100 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                        'text': _('Supprimer les statistiques utilisateur'),
                        'onclick': 'deleteUserStats(event)',
                    },
                    {
                        'type': 'button',
                        'class': 'menu-button col-md-12 mt-4 w-100 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                        'text': _('Enregistrer'),
                        'onclick': 'saveChanges()'
                    }
                ]
            }
        ]
    },
    'settings_es': {
        'menuTitle': 'Cambio de Datos del Usuario',
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
                        'class': 'text-white',
                        'text': _('conectado como PLACEHOLDER')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('victorias')
                    },
                    {
                        'type': 'p',
                        'class': 'text-white',
                        'text': _('derrotas')
                    }
                ]
            },
            {
                'id': 2,
                'type': 'button',
                'class': 'menu-button col-md-12 mt-2 w-25 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                'text': _('ATRÁS'),
                'onclick': 'load_main()'
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
                                'class': 'text-white',
                                'text': _('Elige un nuevo nombre de usuario ')
                            },
                            {
                                'type': 'input',
                                'inputType': 'text',
                                'identifier': 'username',
                                'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                'value': 'placeholder'
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
                                'class': 'text-white',
                                'text': _('Seleccionar nuevo avatar')
                            },
                            {
                                'type': 'select',
                                'name': 'avatar',
                                'class': 'form-control mb-3 bg-secondary bg-gradient text-white',
                                'identifier': 'avatar',
                                'content': [
                                    # Agregue aquí las opciones para los avatares
                                ]
                            },
                        ]
                    },
                    {
                        'type': 'button',
                        'class': 'menu-button col-md-12 mt-2 w-100 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                        'text': _('Eliminar estadísticas del usuario'),
                        'onclick': 'deleteUserStats(event)',
                    },
                    {
                        'type': 'button',
                        'class': 'menu-button col-md-12 mt-4 w-100 h-25 p-3 rounded bg-secondary bg-gradient text-white',
                        'text': _('Guardar'),
                        'onclick': 'saveChanges()'
                    }
                ]
            }
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