'''
Top level definitions of releases to make.
'''
from pathlib import Path

project_dir = Path(__file__).resolve().parents[1]
from Release_Spec_class import Release_Spec

__all__ = [
    'release_specs',
    ]

release_specs = [
    Release_Spec(
        name = 'sn_x4_python_pipe_server_py',
        root_path = project_dir / 'X4_Python_Pipe_Server',
        files = [
            '__init__.py',
            'Main.py',
            'Classes/__init__.py',
            'Classes/Pipe.py',
            'Classes/Server_Thread.py',
        ],
        ),
    
    Release_Spec(
        name = 'sn_x4_python_pipe_server_exe',
        root_path = project_dir / 'X4_Python_Pipe_Server',
        files = [
            '../bin/X4_Python_Pipe_Server.exe',
        ],
        ),
    
    Release_Spec(
        root_path = project_dir / 'extensions/sn_better_target_monitor',
        ),
    
    Release_Spec(
        root_path = project_dir / 'extensions/sn_extra_game_options',
        ),
    
    Release_Spec(
        root_path = project_dir / 'extensions/sn_hotkey_collection',
        ),
    
    Release_Spec(
        root_path = project_dir / 'extensions/sn_remove_dock_symbol',
        ),
    
    Release_Spec(
        root_path = project_dir / 'extensions/sn_station_kill_helper',
        ),
    
    Release_Spec(
        root_path = project_dir / 'extensions/sn_interact_collection',
        ),
    
    Release_Spec(
        root_path = project_dir / 'extensions/sn_mod_support_apis',
        files = [
            'lua_interface.txt',
        ],
        doc_specs = {
            'documentation/Named_Pipes_API.md':[
                'md/Named_Pipes.xml',
                'md/Pipe_Server_Host.xml',
                'md/Pipe_Server_Lib.xml',
                'lua/named_pipes/Interface.lua',
            ],
            'documentation/Hotkey_API.md':[
                'md/Hotkey_API.xml',
            ],
            'documentation/Simple_Menu_API.md':[
                'md/Simple_Menu_API.xml',
            ],
            'documentation/Simple_Menu_Options_API.md':[
                'md/Simple_Menu_Options.xml',
            ],
            'documentation/Time_API.md':[
                'lua/time/Interface.lua',
            ],
        },
        ),

    ]