# zebra-finch-memory

## Data Files

Data is organized into pandas dataframes.

* Subject Data: Information about each subject who took the test

* Trial Data: Subject response data from all trials in the test across all days

* Test Contexts: The stages of the song learning ladder to cross reference with the Trial Data

* Stimulus Files: WAV files played as stimuli during the test, referenced by Trial Data

* Stimulus File Metadata: ?

### Subject Data

### Trial Data

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
|Subject      |String     |             |
|Trial        |Integer    |Trial number (within day) |
|Time         |Datetime   |System time of trial start|
|Date         |Date       |             |
|Interrupt    |Boolean    |True if subject pecked to interrupt playback|
|RT           |Float      |Response time (in seconds)|
|Stimulus File |String           |Path to stimulus wav file|
|Stimulus Vocalizer | String    | Name of vocalizing subject |
|Stimulus Call Type | String    | Call type (SO or DC) |
|Stimulus Class        |String     |"Rewarded" or "Unrewarded"|
|Rewarded     |Boolean    |True if subject received food reward (derived from Class and Interrupt)|
|Informative Trials Seen |Integer |Number of times that a stimulus from this vocalizer had previously been uninterrupted| 
|Test Context |String     | Test context (references Test Context table) |

### Test Context

|Ladder| Test Name   |  # Rewarded Vocalizers |  # Non-rewarded Vocalizers  | Description |
|------|-------------|-----------|-------------|---|
|Week 1 / Week 2      |SovsSo_1v1       | 1 song | 1 song |  |
|      |SovsSo_4v4       | 4 songs (3 new) | 4 songs (3 new) | |
|      |SovsSo_8v8_d1    | 8 songs (4 new) | 8 songs (4 new) | New vocalizers played twice as frequently |
|      |SovsSo_8v8_d2    | 8 songs (equal frequency) | 8 songs | All vocalizers played at equal frequency |
|      |DCvsDC_1v1       | 1 dc | 1 dc | |
|      |DCvsDC_4v4       | 4 dcs (3 new) | 4 dcs (3 new) | |
|      |DCvsDC_6v6_d1    | 6 dcs (2 new) | 6 dc (2 new) | New vocalizers played twice as frequently |
|      |DCvsDC_6v6_d2    | 6 dcs (2 new) | 6 dc (2 new) | All vocalizers played at equal frequency |
|Week 3 / Week 4|SovsSo_1v1_S2       | 1 song | 1 song |  |
|      |SovsSo_4v4_S2       | 4 songs (3 new) | 4 songs (3 new) | |
|      |SovsSo_8v8_d1_S2    | 8 songs (4 new) | 8 songs (4 new) | New vocalizers played twice as frequently |
|      |SovsSo_8v8_d2_S2    | 8 songs (equal frequency) | 8 songs | All vocalizers played at equal frequency |
|      |DCvsDC_1v1_S2       | 1 dc | 1 dc | |
|      |DCvsDC_4v4_S2       | 4 dcs (3 new) | 4 dcs (3 new) | |
|      |DCvsDC_6v6_d1_S2    | 6 dcs (2 new) | 6 dc (2 new) | New vocalizers played twice as frequently |
|      |DCvsDC_6v6_d2_S2    | 6 dcs (2 new) | 6 dc (2 new) | All vocalizers played at equal frequency |
|Week 5|DCvsDC_12v12     | 12 dcs | 12 dcs | Combined stimuli from DCvsDC_6v6_d2 and DCvsDC_6v6_d2_S2 |
|      |SovsSo_16v16     | 16 songs | 16 songs | Combined stimuli from SovsSo_8v8_d2 and SovsSo_8v8_d2_S2 |
|Week 6|AllvsAll_4v4     | 2 songs + 2 dcs | 2 songs + 2 dcs | All vocalizers previously learned in earlier sets (refreshed set) |
|      |AllvsAll_28v28     | 16 songs + 12 dcs | 16 songs + 12 dcs | Combined stimuli from DCvsDC_12v12 and SovsSo_16v16 |


### Stimulus Files

Stimulus .wav files are organized in a directory structure with folders for each of the tests defined in the Test Context table. Paths in the Trial Data reference directories relative to the top level of the `stimuli` folder.
