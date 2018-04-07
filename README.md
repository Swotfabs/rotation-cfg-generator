# Rotation cfg Generagor
A small utitility to create the cfg commands necessary for a Movie Battle II rotation

## Setup
When you download the repository there will be a rotations.json.examples file.
You must create a rotations.json file as the script will be expecting that.

### Json File Format
This section explains the different parts of the json configuration file

```json
{
    "profiles":
    {
        "_description": "Here you put the different rotations for your server",

        "large":
        {
            "_description": "These are the settings you want when the server switches to this rotation",
            "_note": "maps is a list of the maps on the rotation",

            "sv_hostname": "^4/^5/ ^7Resurgence RTV^4/RTM",
            "g_hidehudfromspecs": 1,
            "g_password": "none",
            "shorthand": "ORD",
            "maps":
            [
                {
                    "map": "mb2_corellia",
                    "g_authenticity": 0,
                    "mbmode": 0,
                    "fraglimit": 12,
                    "map_restart_mb": true
                },
                {
                    "map": "mb2_lunarbase",
                    "g_authenticity": 0,
                    "mbmode": 0,
                    "fraglimit": 12,
                    "map_restart_mb": true
                }
            ]
        }
    },
    "defaults":
    {
        "default_commands":
        {
            "_description": "Commands added to every map if not overwritten. Defaults used",
            "commands":
            [
                "roundlimit", "fraglimit"
            ]
        },
        "default_attributes":
        {
            "_description": "Attributes added to every command if not overwritten",
        }
    },
    "commands":
    {
        "_description": "A list of commands supported by the generator.",
        "_note": "default_value refers to the default value of the command. If it is false there is none.",
        "map":
        {
            "_description": "Changes the map",
            "priority": 2,
            "string": "map \"{}\"",

            "default_value": false
        },
        "g_authenticity":
        {
            "_description": "In conjuntion with mbmode changes the mode of the game (Open, Semi-FA, FA)",
            "priority": 1,
            "string": "g_authenticity \"{}\"",

            "default_value": false
        },
        "mbmode":
        {
            "_description": "In conjuntion with mbmode changes the mode of the game (Open, Semi-FA, FA)",
            "_note": "This will be used instead of the map command",
            "priority": 1,
            "string": "mbmode \"{}\" \"{}\"",

            "default_value": false
        },
        "roundlimit":
        {
            "_description": "When the total rounds reaches this amount, the map ends. Ties may happen",
            "priority": 3,
            "string": "roundlimit \"{}\"",

            "default_value": 12
        },
        "fraglimit":
        {
            "_description": "If a team reaches this amount of won rounds, it wins the map",
            "priority": 3,
            "string": "fraglimit \"{}\"",

            "default_value": 12
        },
        "map_restart_mb":
        {
            "_description": "Restarts the map",
            "priority": "end",
            "string": "map_restart_mb",

            "default_value": true
        },
        "sv_hostname":
        {
            "_description": "Changes the name of the server",
            "string": "set sv_hostname \"{}\"",

            "default_value": "^4/^5/ ^7Resurgence RTV^4/RTM"
        },
        "g_hidehudfromspecs":
        {
            "_description": "Spectators cannot see the HUD of others",
            "string": "set g_hidehudfromspecs \"{}\"",

            "default_value": 1
        },
        "g_password":
        {
            "_description": "Sets the password players need to join the server",
            "string": "set g_password \"{}\"",

            "default_value": "none"
        }
    }
}
```
