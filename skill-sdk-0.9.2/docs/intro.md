# Introduction

The Smart Voice Hub Skill SDK for Python is a Python package that assists in creating skill implementations for the
Smart Voice Hub in Python.

It contains 

- a set of Python modules that will create a microservice serving the skill, 
- a wrapper that abstracts the HTTP calls into Python function call, 
- some helpful libraries, 
- a few scripts and 
- other useful contributions.

SDK for Python tries to handle the [Skill SPI](https://smarthub-wbench.wesp.telekom.net/pages/smarthub_cloud/skill-spi/public/index.html) (Service Provider Interface).  
The SPI defines the communication between CVI core and the skills.  
This SPI is maintained by the CVI core developers and represents the current interface between the CVI core and the skills.

**Further information**

- [Skill SPI](https://smarthub-wbench.wesp.telekom.net/gitlab/smarthub_cloud/skill-spi)
- [Skill SPI Documentation](https://smarthub-wbench.wesp.telekom.net/pages/smarthub_cloud/skill-spi/public/index.html)
- [Skill API Documentation](https://smarthub-wbench.wesp.telekom.net/pages/smarthub_cloud/svh-cloud-doc/public/skill-api/skill-api.html)
- [Changelog](https://smarthub-wbench.wesp.telekom.net/gitlab/smarthub_cloud/skill-spi/blob/master/CHANGELOG.md)
- Example requests/responses as JSON files:
    - [Skill info - SkillInfoResponseDto](https://smarthub-wbench.wesp.telekom.net/gitlab/smarthub_cloud/skill-spi/blob/master/src/test/resources/serialized/SkillInfoResponseDto.json)
    * [Skill invoke - InvokeSkillRequestDto](https://smarthub-wbench.wesp.telekom.net/gitlab/smarthub_cloud/skill-spi/blob/master/src/test/resources/serialized/InvokeSkillRequestDto.json)
    * [Skill response - InvokeSkillResponseDto](https://smarthub-wbench.wesp.telekom.net/gitlab/smarthub_cloud/skill-spi/blob/master/src/test/resources/serialized/InvokeSkillResponseDto.json)

