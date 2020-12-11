Supported `kit_names`
=====================

* `system`: see System section
* `telephony`: see Telephony section
* `audio_player`; see AudioPlayer section
* `timer`: see Timer section
* `tv`: see tv section

The `text` field from the result must always be uttered via TTS (if cloud tts is unavailable).

System
======

Actions
-------

* `stop`: Will send a `Stop` Event. This means stopping the foreground activity on the device. If there was another activity in background, it will gain focus.

  Parameters:

  * `skill` (string, optional) in is set, a `{skill}Stop` event (stopping the related activity).
    Currently supported skills: `Timer`, `Conversation`, `Media`

> To stop current activity:
>  ```python
>  data = {
>      "use_kit": {
>          "kit_name": "system",
>          "action": "stop"
>      }
>  }
>
>  return Response(text=msg, result=Result(data)) 
> ``` 

* `resume`: Will resume media (if paused). No parameters are used.

* `pause`: Pause currently active content (if supported)

* `next`: Execute next track in content channel

* `previous`: Go to previous track in content channel

* `open_source`: start open source readout

* `say_again`: Repeat lastly uttered sentence (from the dialog channel)

* `volume_down`, `volume_up`: decrease (increase) volume (by an unspecified amount)

* `volume_to`: set absolute volume
  Parameters:
  * `value` (integer from [0-10]), specifying the volume level

> Set volume to a middle level:
> ```python
> data = {
>     "use_kit": {
>         "kit_name": "system",
>         "action": "volume_to",
>         "parameters": {
>             "value": 5
>         }
>     }
> }
>
> return Response(text=msg, result=Result(data)) 
> ``` 

* `bluetooth_pairing`: Enable bluetooth paring (Devoice should become discoverable)

AudioPlayer
===========

Actions
-------

* `play_stream`: Play the specified stream in `stream_url`.

  Parameters:
  * `url` (string): URI related to the audio played

> Play a stream from `stream_url`:
> ```python
> data = {
>     "use_kit": {
>         "kit_name": "audio_player",
>         "action": "play_stream",
>         "parameters": {
>             "url": stream_url
>         }
>     }
> }
>
> return Response(text=msg, result=Result(data)) 
> ``` 

* `play_stream_before_text`: Play a stream, followed by the text specified in `text` (in the result, not as part of the kit parameters).
  *Info*: Currently broken on the smart speaker (premium)

* `pause`: pauses playback in the content channel

  Parameters:
  * `content_type` (string): Possible value: `radio`. If set, will stop radio (and not pause).
  * `not_playing` (string): Text to be played after media stopped. Only evaluated when `content_type` is `radio`

* `resume`: Resume paused media

  Parameters:
  * `content_type` (string): Possible value: `radio`. If set, will restart radio.
  *Info*: likely broken for other content types than `radio`.

* `stop`: Stop any currently active media (spotify, radio, content tts).

  Parameters:
  * `not_playing` (string): TTS to be uttered before stopping the radio.

* `disco_disco`

Timer
=====

Actions
-------

* `set_timer`, `cancel_timer`: Both actions cause an update/fetch of the current timer configuration

> Stop currently counting timer:
> ```python
> data = {
>     "use_kit": {
>         "kit_name": "timer",
>         "action": "cancel_timer"
>     }
> }
>
> return Response(text=msg, result=Result(data)) 
> ``` 

Telephony
=========

Actions
-------

* `accept_call`: Accept an incoming call.

* `call_extern`: Call an external number.

    Parameters:
  * `number` (string): telephone number to call
  * `contact` (string, optional): contact name in address book

* `call_last_incoming_call`: Call last incoming call.
  TTS in `text` field is uttered before action.

* `call_last_missed_call`: Call back last missed incoming call.
  TTS in `text` field is uttered before action.

* `call_last_outgoing_call`: Call last outgoing number again
  TTS in `text` field is uttered before action.

* `deregister`: Unpair the DECT telephone.

* `hang_up`: Hang up the current call or refuse a ringing call.

  Parameters:
  * `notify` (dict of strings). Requires key `TELEPHONY_HANGUP_CALL_CONFIRM` for TTS playback for hangout acknowledge after hanging up the call.

* `ignore_call`: Will ignore an incoming call and speak the TTS given in the `text` field.

* `press_key`: Send a single or multiple DTMF keys.

  Parameters:
  * `keys` (sequence of characters): DTMF codes. Valid characters are digits (0-9), `#`, and `*`.

* `refuse_call`: Identical to `hang_up`.

* `start_pairing`: Will play TTS given in `text` and start the DECT pairing process

tv
==
For all tv actions you have to send the acces_token as Parameter

* `entpairing`: Reset the stored verification_code and udn. Inform the user that the box is unpaired.

* `pairing`: Pair your Entertain TV with the Smart Voice Hub in the Smart Voice Hub App.

* `switch_channel`: switch betweeen channels via channel name or channel number.
    
    Parameters:
        
    * `channel`: channel
    * `channel_type`: channel_type

* `remote_key`: Action for imitate the entertain controller.

    Parameters:
    * `keys`
        
        TV__Fast_Forward
            
            'keys': [{'code': FAST_FORWARD_KEY_CODE, 'value': FAST_FORWARD_KEY_VALUE}]}
        
        TV__POWER
        
            'keys': [{'code': POWER_ON_KEY_CODE, 'value': POWER_ON_KEY_VALUE}]
        
        ENTERTAIN_RETURN_KEY
        
            'keys': [{'code': key_maps.BACK_KEY_CODE, 'value': key_maps.BACK_KEY_VALUE}]
        
        ENTERTAIN_NAVIGATION_KEY
        
            ‚keys': [{'code': key_code, 'value': key_value}]
        
        ENTERTAIN_OK_KEY
        
            'keys': [{'code': key_maps.OK_KEY_CODE, 'value': key_maps.OK_KEY_VALUE}]
        
        ENTERTAIN_POWER_ON-OFF
        
            ‚keys': [{'code': key_code, 'value': key_value}]
        #### List of all keys:
        
        + STB Key commands (UPNP)
        ON_OFF_KEY_CODE = 'On/Off'
        
        + ON_OFF_KEY_VALUE = '0x0100'
        POWER_ON_KEY_CODE = 'PowerOn'
        
        + POWER_ON_KEY_VALUE = '0x480'
        POWER_OFF_KEY_CODE = 'PowerOff'
        
        + POWER_OFF_KEY_VALUE = '0x481'
        NUM0_KEY_CODE = '0'
        
        + NUM0_KEY_VALUE = '0x0030'
        NUM1_KEY_CODE = '1'
        
        + NUM1_KEY_VALUE = '0x0031'
        NUM2_KEY_CODE = '2'
        
        + NUM2_KEY_VALUE = '0x0032'
        NUM3_KEY_CODE = '3'
        
        + NUM3_KEY_VALUE = '0x0033'
        NUM4_KEY_CODE = '4'
        
        + NUM4_KEY_VALUE = '0x0034'
        NUM5_KEY_CODE = '5'
        
        + NUM5_KEY_VALUE = '0x0035'
        NUM6_KEY_CODE = '6'
        
        + NUM6_KEY_VALUE = '0x0036'
        NUM7_KEY_CODE = '7'
        
        + NUM7_KEY_VALUE = '0x0037'
        NUM8_KEY_CODE = '8'
        
        + NUM8_KEY_VALUE = '0x0038'
        NUM9_KEY_CODE = '9'
        
        + NUM9_KEY_VALUE = '0x0039'
        BACK_KEY_CODE = '<X'
        
        + BACK_KEY_VALUE = '0x002E'
        TEXT_KEY_CODE = 'Text'
        
        + TEXT_KEY_VALUE = '0x0560'
        SPACE_KEY_CODE = ' '
        
        + SPACE_KEY_VALUE = '0x0113'
        SEARCH_KEY_CODE = 'Search'
        
        + SEARCH_KEY_VALUE = '0x0451'
        HOME_KEY_CODE = 'Home'
        
        + HOME_KEY_VALUE = '0x0110'
        MUSIC_KEY_CODE = 'Music'
        
        + MUSIC_KEY_VALUE = '0x0462'
        EPG_KEY_CODE = 'EPG'
        
        + EPG_KEY_VALUE = '0x0111'
        OPT_KEY_CODE = 'Opt.'
        
        + OPT_KEY_VALUE = '0x0460'
        UP_KEY_CODE = 'Up'
        
        + UP_KEY_VALUE = '0x0026'
        DOWN_KEY_CODE = 'Down'
        
        + DOWN_KEY_VALUE = '0x0028'
        LEFT_KEY_CODE = 'Left'
        
        + LEFT_KEY_VALUE = '0x0025'
        RIGHT_KEY_CODE = 'Right'
        
        + RIGHT_KEY_VALUE = '0x0027'
        OK_KEY_CODE = 'Ok'
        
        + OK_KEY_VALUE = '0x000D'
        BACK_KEY_CODE = 'Back'
        
        + BACK_KEY_VALUE = '0x0008'
        EXIT_KEY_CODE = 'Exit'
        
        + EXIT_KEY_VALUE = '0x045D'
        VOL_UP_KEY_CODE = 'Vol+'
        
        + VOL_UP_KEY_VALUE = '0x0103'
        VOL_DOWN_KEY_CODE = 'Vol-'
        
        + VOL_DOWN_KEY_VALUE = '0x0104'
        INFO_KEY_CODE = 'i'
        
        + INFO_KEY_VALUE = '0x010C'
        MUTE_KEY_CODE = 'Mute/Unmute'
        
        + MUTE_KEY_VALUE = '0x0105'
        CHANNEL_UP_KEY_CODE = 'P+'
        
        + CHANNEL_UP_KEY_VALUE = '0x0101'
        CHANNEL_DOWN_KEY_CODE = 'P-'
        
        + CHANNEL_DOWN_KEY_VALUE = '0x0102'
        REWIND_KEY_CODE = '<<'
        
        + REWIND_KEY_VALUE = '0x0109'
        FAST_FORWARD_KEY_CODE = '>>'
        
        + FAST_FORWARD_KEY_VALUE = '0x0108'
        RECORD_KEY_CODE = 'REC'
        
        + RECORD_KEY_VALUE = '0x0461'


* `record`: Record current live program or specific channel/tv-show

    Parameters:
    
    example
        
        "attributes": {
        
        channel": ["ZDF"],
        
        "tv_keyword": ["Tatort"]
        
        }
    or:
        
        "record_type": 'current_channel'





* `volume`: Control the Volume on the TV. You can set the volume up and down.

    parameters:
    
    * `value`: 'up'
    * `value`: 'down'

* `pause`: Streams can be paused and played again.



* `play`



* `search`

    Parameter:

    * `search_query`: ['Brad Pitt']