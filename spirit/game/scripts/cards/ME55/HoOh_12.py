from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="15494b14-49f0-51f6-addb-6b66ba983900",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOh.Name",
    display_name="Ho-Oh",
    searchable_by=["Ho-Oh", "Basic", "HoOh"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="ME55",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=250,
    abilities=[
        Attack(
            title="Sacred Breath",
            game_text="Discard all Energy from this Pok\u00e9mon. Heal all damage from 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Fire Wing",
            cost={PokemonTypes.FIRE: 3},
            damage=100,
        ),
    ],
)