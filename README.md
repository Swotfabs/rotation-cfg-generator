# Rotation cfg Generagor
A small utitility to create the cfg commands necessary for a Movie Battle II rotation

## Setup
When you download the repository there will be a rotations.json.examples file.
You must create a rotations.json file as the script will be expecting that.

### Json File Format
This section explains the different parts of the json configuration file

```
{
    // This section defines what commands the configuration generator will be able to interpret
    "commands":
    {
        // Each command's name is that which it will be in the cfg line
        "map":
        {
            // The priority value is where in the cfg line it needs to be, lower priority coming first
            "priority": 2,

            // The string value determines how the cfg command will be inserted.
            // The {} is where the value will be inserted.
            "string": "map \"{}\"",

            // This sets whether this command has a default value.
            // This will either be true, false, or a value.
            // You can obviously change these as desired.
            // false means the command has no default value
            "default": false
        },
        "g_authenticity":
        {
            "priority": 1,
            "string": "g_authenticity \"{}\"",
            "default": false
        },
        "mbmode":
        {
            "priority": 1,
            "string": "mbmode \"{}\"",
            "default": false
        },
        "fraglimit":
        {
            "priority": 3,
            "string": "fraglimit \"{}\"",

            // A value means that the command has a default, and it is that value.
            // For example, if fraglimit is not defined in one of the maps below it will be set to 12.
            "default": 12
        },
        "map_restart_mb":
        {
            "priority": "end",
            "string": "map_restart_mb",

            // True denotes a command that has no value and will either exist or not exist
            "default": true
        }
    },
    // This holds the different rotation profiles, each profile will be a rotation the server can be set to
    "rotations":
    {
        // Each profile will have a name
        "large":
        {
            "name": "large",

            // The shorthand is the name of the vstr that this rotation will have
            "shorthand": "ORD",

            // This is a list of maps, in order, in this rotation.
            "maps":
            [
                {
                    // Here go all of the settings for this map.
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
    }
}
```
