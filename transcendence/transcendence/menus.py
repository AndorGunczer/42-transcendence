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
                        'label': 'LOGO',
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
        'menuItems': [
            {
                'id': 1,
                'label': 'BACK',
                'action': 'load_main()'
            },
            {
                'id': 2,
                'label': 'SINGLEPLAYER',
                'action': 'single_pregame()'
            },
            {
                'id': 3,
                'label': 'LOCAL',
                'action': 'local_pregame()'

            },
            {
                'id': 4,
                'label': 'ONLINE',
                'action': 'online_pregame()'
            },
        ]
    }
}