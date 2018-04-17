# Rotation cfg Generagor
A small utitility to create the cfg commands necessary for a Movie Battle II rotation

## Setup
When you download the repository there will be a rotations.json.examples file.
You must create a rotations.json file as the script will be expecting that.

### Profiles
Here you describe the various rotation profiles you have and the maps in them.
The program looks for a profiles.json.
profiles.json.example is provided as a working example you can copy and edit.

```json
{
    "profiles":
    {
        "_description": "Here you put the different rotations for your server",

        "large":
        {
            "_description": "These are the settings you want when the server switches to this rotation",
            "_note": "maps is the list of the maps on the rotation",

            "sv_hostname": "€€€€€€€ ^4/^5/ ^7RESURGENCE rtv^4/^5/^7rtm",
            "g_hidehudfromspecs": 0,
            "g_password": "none",
            "shorthand": "ORD",
            "maps":
            [
                {
                    "map": "mb2_corellia",
                    "mbmode": 0,
                    "fraglimit": 12,
                    "g_allowedVillainClasses": 0,
                    "g_allowedHeroclasses": 0
                },
                {
                    "map": "mb2_lunarbase",
                    "mbmode": 0,
                    "fraglimit": 12,
                    "g_allowedVillainClasses": 0,
                    "g_allowedHeroclasses": 0
                }
            ]
        }
    }
}
```

### Defaults
Here you describe the defaults of commands if you do not provide a value.
The program looks for a defaults.json.
defaults.json.example is provided as a working example you can copy and edit.

```json
{
    "defaults":
    {
        "default_commands":
        {
            "_description": "Commands added to every map if not overwritten. Default values used",
            "commands":
            [
                "roundlimit", "fraglimit", "g_authenticity", "g_allowedVillainClasses", "g_allowedHeroclasses"
            ]
        },
        "default_attributes":
        {
            "_description": "Attributes added to every command if not overwritten"
        },
        "commands":
        {
            "_description": "If a map specifies a command with no value, these will be used",
            "_note": "If the command does not have a default value, it is marked as null",
            "g_authenticity": null,
            "map": null,
            "mbmode": 0,
            "fraglimit": 12,
            "roundlimit": 12,
            "g_allowedVillainClasses": 0,
            "g_allowedHeroclasses": 0,
            "map_restart_mb": true,
            "sv_hostname": "^4/^5/ ^7Resurgence RTV^4/RTM",
            "g_hidehudfromspecs": 1,
            "g_password": "none"
        }
    }
}
```