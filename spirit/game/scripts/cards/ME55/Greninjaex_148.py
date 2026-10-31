from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="173ee17f-e55f-5b8d-bddb-4d4d5a392f76",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greninjaex.Name",
    display_name="Greninja ex",
    searchable_by=["Greninja ex", "Stage 2", "ex", "Greninjaex"],
    subtypes=["Stage 2", "ex"],
    collector_number=148,
    set_code="ME55",
    rarity=Rarities.Rare,
    hp=300,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    family_id=658,
    abilities=[
        Attack(
            title="Stealthy Slash",
            game_text="This attack does 30 damage to 1 of your opponent's Pok\u00e9mon for each damage counter on that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Aqua Edge",
            cost={PokemonTypes.WATER: 2},
            damage=160,
        ),
    ],
)