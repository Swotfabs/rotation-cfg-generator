# Rotation cfg Generagor
A small utitility to create the cfg commands necessary for a Movie Battle II rotation

## Setup
When you download the repository there will be a rotations.json.examples file.
You must create a rotations.json file as the script will be expecting that.

### Json File Format
This section explains the different parts of the json configuration file

```json
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
            "string": "map \"{}\""
        },
        "g_authenticity":
        {
            "priority": 1,
            "string": "g_authenticity \"{}\""
        },
        "mbmode":
        {
            "priority": 1,
            "string": "mbmode \"{}\""
        },
        "fraglimit":
        {
            "priority": 3,
            "string": "fraglimit \"{}\""
        },
        "map_restart_mb":
        {
            "priority": "end",
            "string": "map_restart_mb"
        }
    },
    "rotations":
    {
        "large":
        {
            "name": "large",
            "shorthand": "ORD",
            "maps":
            [
                {
                    "map": "mb2_corellia",
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
