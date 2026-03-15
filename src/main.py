import asyncio
from viam.module.module import Module
from models.generic_component import GenericComponent


if __name__ == '__main__':
    asyncio.run(Module.run_from_registry())
