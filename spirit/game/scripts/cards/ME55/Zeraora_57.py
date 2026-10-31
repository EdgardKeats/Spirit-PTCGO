from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e8ebe1aa-095b-5a13-9d34-8f358edd5465",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zeraora.Name",
    display_name="Zeraora",
    searchable_by=["Zeraora", "Basic", "Zeraora"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="ME55",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=807,
    abilities=[
        Attack(
            title="Rapid Draw",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Electrobullet",
            game_text="This attack also does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)