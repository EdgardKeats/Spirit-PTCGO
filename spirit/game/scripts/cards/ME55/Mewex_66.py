from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6e738228-cc53-5b1f-b24f-8863605081ae",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewex.Name",
    display_name="Mew ex",
    searchable_by=["Mew ex", "Basic", "ex", "Mewex"],
    subtypes=["Basic", "ex"],
    collector_number=66,
    set_code="ME55",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=151,
    abilities=[
        Ability(
            title="Memory Helix",
            game_text="This Pok\u00e9mon can use the attacks of any of your Benched Pok\u00e9mon. (You still need the necessary Energy to use each attack.)",
            effect=unimplemented,
        ),
        Attack(
            title="Teleportation Burst",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)